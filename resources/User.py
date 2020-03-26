from app import  api,Resource, fields
from models.userModel import UserModel,user_schema,users_schema

#define my namespaces

ns_users=api.namespace('users', description="All opartation of users")


user_model=api.model('Users',{
    'fullname':fields.String(),
    'email':fields.String(),
    'password':fields.String()

})


@ns_users.route('')
class UserList(Resource):
    def get(self):
        """Use this Endpoint to get all users"""
        users=UserModel.fetch_all()
        return users_schema.dump(users),200



@ns_users.route('/<int:id>')
class Users(Resource):
    def get(self,id):
        """Get user by id"""
        user= UserModel.fetch_all(id)
        return users_schema.dump(user),200

    def put(self,id):
        """Edit a new user by id """
        pass

    def delete(self,id):
        """Delete user by id"""
        user=UserModel.fetch_all(id)
        if user:
            user.delete_from_db()
            return {"Message":'User Deleted Successfully'}
        else:
            return {"Message":'The User does not exist'}


