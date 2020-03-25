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
        return users_schema.dump(users)

    @api.expect(user_model)
    def post(self):
        """Add a new user"""
        data= api.payload
        users=UserModel(
            fullname=data["fullname"],
            email=data['email'],
            password=data['password']

        )
        users.save_toDB()
        return  user_schema.dump(users),201

@ns_users.route('/<int:id>')
class Users(Resource):
    def get(self,id):
        """Get user by id"""
        pass

    def put(self,id):
        """Edit a new user by id """
        pass

    def delete(self,id):
        """Delete user by id"""



