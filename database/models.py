from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    birthday = Column(Integer)


class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer, unique=True)
    birthday = Column(Integer)
    expirience = Column(Integer)
    salary = Column(Integer, default=0)
    teacher_subject = Column(String)

class Homework(Base):
    __tablename__ = 'homeworks'

    homework_id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    homework_published_date = Column(DateTime)
    homework_deadline = Column(DateTime)
    subject = Column(String)
    title = Column(String)
    description = Column(String)

