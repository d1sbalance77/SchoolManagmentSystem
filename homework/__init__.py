from pydantic import BaseModel



class AddNewHomeworkValidator(BaseModel):
    homework_id: int
    mark: int
    homework_published_date: int
    homework_deadline: int
    subject: str
    title: str
    description: str




class EditHomeworkInfoValidator(BaseModel):
    homework_id: int
    edit_info: str
    new_info: str

class DeleteHomeworkValidator(BaseModel):
    homework_id: int


