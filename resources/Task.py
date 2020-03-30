from app import  api,Resource, fields,jwt_required,get_jwt_identity
from models.taskmodel import TaskModel,task_schema,tasks_schema
from  models.userModel import UserModel,users_schema,user_schema
#define my namespaces

ns_tasks=api.namespace('tasks', description="All opartation of tasks")

#documenting
#models
a_task_model =api.model( 'Task',{
    'title':fields.String(),
    'description':fields.String()

})

# tasks= [
#     {"id":1, "title":"Learn Javascript", "description":"Learning Basics"},
#     {"id":2, "title":"Learn Python", "description":"Learning Basics"},
#     {"id":3, "title":"Learn PHP", "description":"Learning Basics"}
# ]

# @api.route('/tasks')
@ns_tasks.route('')
class TaskList(Resource):

    @api.doc(security='apikey')
    @jwt_required
    def get(self):
        """Use  this endpoint to get all the tasks"""
        # tasks=TaskModel.fetch_all()
        user_id=get_jwt_identity()
        user=UserModel.get_userby_id(user_id)
        user_tasks =user.tasks
        return tasks_schema.dump(user_tasks),200

    @api.doc(security='apikey')
    @api.expect(a_task_model) #use Jwt requierd to prevent  """
    @jwt_required
    def post(self):
        """Use this end point to add a new task"""
        # data["id"]=len(tasks)+1
        # tasks.append(data)
        # return  data ,201

        data = api.payload
        task=TaskModel(title=data["title"],description=data["description"],
                       user_id=get_jwt_identity()) #to get the id of the logged on person
        task.save_toDB()
        return  task_schema.dump(task),201

# create a route for getting a single task by ID
# @api.route('/tasks/<int:id>')
@ns_tasks.route('/<int:id>')
class Task(Resource):

    @api.doc(security='apikey')#makes the def methods require api token to be authorized
    @api.expect(a_task_model)
    @jwt_required
    def get(self,id):
        """get task by Id"""

        # a_task= next(filter(lambda x: x['id']==id,tasks),None)

        tasks = TaskModel.fetch_all()
        task=next(filter(lambda x :x.id==id,tasks),None)
        return task_schema.dump(task),200
    @jwt_required
    def put(self,id):
        """Edit a task  by its Id """
        data= api.payload
        # task= next(filter(lambda x: x['id']==id,tasks),None)
        tasks = TaskModel.fetch_all()
        task = next(filter(lambda x: x.id == id, tasks), None)

        if task:
            if u'title' in data:
                task.title=data['title']
            if u'description' in data:
                task.description= data['description']

            task.save_toDB()
            return {"Message":"Updated successfully"} ,200

        return {"message":"Task not found"},404

    @jwt_required
    def delete(self, id):
        """delete a task by Id"""
        tasks= TaskModel.fetch_all()
        task= next(filter(lambda x: x.id==id,tasks),None)
        if task:
            task.delete_from_db()
            return {'message':'Task successfully deleted'},200
        else:
            return {'message':'Task not found'},404
