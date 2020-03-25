from app import db,ma
from app import  SQLAlchemy

from sqlalchemy import func


class UserModel(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), nullable=False)
    tasks= db.relationship('TaskModel',backref='user',lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    def save_toDB(self):
        db.session.add(self)
        db.session.commit()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "fullname", "email")

user_schema= UserSchema()
users_schema=UserSchema(many=True)