from pydantic import BaseModel,EmailStr
from typing import Optional


# class GetAllStudentsValidator(BaseModel):
#     pass

class GetExactStudentValidator(BaseModel):
    student_id: int

class AddNewStudentValidator(BaseModel):
    student_id: int
    name: str
    surname: str
    phone_number: int
    email: EmailStr
    city: str
    birthday: int

class EditStudentInfoValidator(BaseModel):
    student_id: int
    edit_info: str
    new_info: str

class DeleteStudentValidator(BaseModel):
    student_id: int