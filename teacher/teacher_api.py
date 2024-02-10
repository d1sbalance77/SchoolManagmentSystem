from fastapi import APIRouter
from teacher import (
    GetAllTeachersValidator,
    GetExactTeacherValidator,
    AddNewTeacherValidator,
    EditTeacherInfoValidator,
    DeleteTeacherValidator,
)
from database.teacher_service import (
    get_all_teachers_db,
    get_exact_teacher_info,
    add_new_teacher_db,
    edit_teacher_info_db,
    delete_teacher_db,
    get_exact_teacher_subject,
)

teacher_router = APIRouter(prefix='/teacher', tags=['Teacher'])

# Get all teachers
@teacher_router.get('/get-all-teachers')
async def get_all_teachers_DataBase():

    return get_all_teachers_db()

# Get exact teacher by ID
@teacher_router.get('/exact-teacher/{teacher_id}')
async def get_exact_teacher_endpoint(teacher_id: int):
    result = get_exact_teacher_info(teacher_id=teacher_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Учитель не найден'}


@teacher_router.get('/exact-teacher-subject/')
async def get_exact_teacher_SubJect(teacher_id: int):
    result = get_exact_teacher_subject(teacher_id)

    if result:
        return {'teacher_subject': result}
    else:
        return {'message': 'Учитель и его предмет не найден'}










# Add new teacher
@teacher_router.post('/add-teacher', response_model=str)
async def add_new_teacher(data: AddNewTeacherValidator):
    result = add_new_teacher_db(
        data.name,
        data.surname,
        data.phone_number,
        data.email,
        data.expirience,
        data.teacher_subject,
        data.salary
    )
    return result

# Edit teacher info
@teacher_router.put('/edit-teacher/{teacher_id}', response_model=str)
async def edit_teacher_info(data: EditTeacherInfoValidator):

    result = edit_teacher_info_db(data.teacher_id, data.edit_info, data.new_info)
    return result

# Delete teacher
@teacher_router.delete('/delete-teacher/{teacher_id}')
async def delete_teacher(teacher_id: int):
    result = delete_teacher_db(teacher_id)

    return result
