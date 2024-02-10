from pydantic import BaseModel
from datetime import datetime, timedelta


# class GetExactHomeworkValidator(BaseModel):
#     homework_id: int

class AddNewHomeworkValidator(BaseModel):
    homework_id: int
    subject: str
    title: str
    description: str
    homework_deadline: int
    homework_published_date: int
    mark: int

class EditHomeworkInfoValidator(BaseModel):
    homework_id: int
    edit_info: str
    new_info: str

class DeleteHomeworkValidator(BaseModel):
    homework_id: int


