from fastapi import FastAPI
from homework.homework_api import homework_router
from student.student_api import student_router
from teacher.teacher_api import teacher_router
from database import Base,engine

Base.metadata.create_all(bind=engine)


app = FastAPI(title='SchoolManagmentSystem', docs_url='/')

app.include_router(homework_router)
app.include_router(student_router)
app.include_router(teacher_router)