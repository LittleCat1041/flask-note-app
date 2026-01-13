from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #สร้างความสัมพันธ์ให้ User หนึ่งคนสามารถเป็นเจ้าของ Note ได้หลายรายการ
    #โดย SQLAlchemy จะช่วยดึงข้อมูล Notes ทั้งหมดของ User ให้อัตโนมัติเมื่อเรียกใช้
    notes = db.relationship('Note')