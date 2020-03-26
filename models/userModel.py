from app import db,ma
from app import  SQLAlchemy

from sqlalchemy import func
from  werkzeug.security import check_password_hash


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

    @classmethod
    def check_email_exists(cls,email):
        record=cls.query.filter_by(email=email).first()
        if record:
            return  True
        else:
            return  False

    @classmethod
    def validate_password(cls,email,password):
        record = cls.query.filter_by(email=email).first()
        if record and check_password_hash(record.password,password):
            return True
        else:
            return False

    @classmethod
    def get_user_id(cls,email):
        record= cls.query.filter_by(email=email).first().id
        return record

    @classmethod
    def get_userby_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def save_toDB(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "fullname", "email")

user_schema= UserSchema()
users_schema=UserSchema(many=True)