from app import db,ma
from app import  SQLAlchemy

from sqlalchemy import func


class TaskModel(db.Model):
    __tablename__='tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    completed = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    # @classmethod
    # def fetch_by_id(cls, id):
    #     return cls.query.all()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_toDB(self):
        db.session.add(self)
        db.session.commit()


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description","user_id")


task_schema = TaskSchema()
#serialization of many sqlachemy objects in json arrays
tasks_schema = TaskSchema(many=True)