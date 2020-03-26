from app import  api,Resource, fields,create_access_token
from models.userModel import UserModel,user_schema,users_schema
from werkzeug.security import   generate_password_hash

ns_userLogin = api.namespace('login',description=" Login Details")
ns_registration = api.namespace('register',description="Registration Details")


register_model= api.model('Register Credentials',{
    'firstname':fields.String(),
    'email':fields.String(),
    'password':fields.String()

})
login_model= api.model('Login Credentials',{

    'email':fields.String(),
    'password':fields.String()

})


@ns_registration.route('')
class Registration(Resource):
    @api.expect(register_model)
    def post(self):
        """Add a new user"""
        data = api.payload
        users = UserModel(
            fullname=data["firstname"],
            email=data['email'],
            password= generate_password_hash(data['password'])

        )
        users.save_toDB()
        return user_schema.dump(users), 201

@ns_userLogin.route('')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data= api.payload
        if UserModel.check_email_exists(data['email']):
            if UserModel.validate_password(data['email'],data['password']):
                #after a successful login
                uid=UserModel.get_user_id(data['email'])
                token= create_access_token(identity=uid)
                return {'access_token':token},200
            else:
                return {'Message':'incorrect login credentials'},401
        else:
            return {'Message':'incorrect login credentials'},401