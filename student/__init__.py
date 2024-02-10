from pydantic import BaseModel,EmailStr




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
    new_name: str
    new_birthday: int

class DeleteStudentValidator(BaseModel):
    student_id: int