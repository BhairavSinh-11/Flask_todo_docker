from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    task=db.Column(db.String(200),nullable=False)
    iscompleted=db.Column(db.Boolean,nullable=False,default=False)