from pydantic import BaseModel,EmailStr


class GetExactTeacherValidator(BaseModel):
    teacher_id: int

class AddNewTeacherValidator(BaseModel):
    teacher_id: int
    name: str
    surname: str
    email: EmailStr
    phone_number: int
    expirience: int
    salary: int
    teacher_subject: str

class EditTeacherInfoValidator(BaseModel):
    teacher_id: int
    edit_info: str
    new_info: str

class DeleteTeacherValidator(BaseModel):
    student_id: int