import unittest
import json
from werkzeug.security import generate_password_hash
from Config.Config import Testing

from models.userModel import UserModel
from models.taskmodel import TaskModel
from app import  app,db


class TestLogin(unittest.TestCase):


    def setUp(self):
        db.create_all()
        user=UserModel(fullname="TestUser",email='test@gmail.com',password=generate_password_hash("test"))
        user.created_at()


        def tearDown():
            db.session.remove()
            db.drop_all()

        self.app=app.test_client()
        self.db=db.get_db()


    def test_successful_signup(self):
        #Given
        payload= json.dumps({
            "email":"jkila@gmail.com",
            "password":"mycool"

        })
        response= self.client.post('/login', headers={"Content-Type":"application/json"}, data=payload)
        #
        self.assertEqual(response.status_code,200)
        self.assertEqual(type(response.json['access_token']),str)
        self.assertEqual(response.is_json,True)

        #
    def test_unsuccessful_login(self):
        #given
        payload=json.dumps({"email":"test@gmail.com","password":"334"})
        response= self.client.post('/login', headers={"Content-Type":"application/json"}, data=payload)

        #
        self.assertEqual(response.status_code,401)




    def test_invalid_payLoad(self):
        #given an issue in email key in your payload
        payload= json.dumps({"emai":"test@gmail.com","password":"123"})
        response= self.client.post('/login', headers={"Content-Type":"application/json"}, data=payload)

        #Then
        self.assertEqual(response.status_code,400)

if __name__ == '__main__':
    unittest.main()