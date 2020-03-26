
from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow
from Config.Config import Development
from  flask_jwt_extended import  jwt_required,create_access_token,JWTManager,get_jwt_identity



app = Flask(__name__)

api= Api(app, author='Stan',title='TASK_MANAGEMENT_API', description="A simple task management api", version='1.0.0')
app.config.from_object(Development)

db = SQLAlchemy(app)
ma=Marshmallow(app)

#instanciate Jwt manager
jwt=JWTManager(app)
from models.taskmodel import TaskModel

@app.before_first_request
def create_all():
    db.create_all()


from resources.Task import *
from resources.User import *
from resources  .registrationLogin import *





if __name__ == '__main__':
    app.run(debug=True)
