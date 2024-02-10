from fastapi import APIRouter
from homework import (

    # GetExactHomeworkValidator,
    AddNewHomeworkValidator,
    # EditHomeworkInfoValidator,
    # DeleteHomeworkValidator,

)

from database.homework_service import (

    get_exact_homework,
    add_new_homework_db,
    edit_homework_info_db,
    delete_homework_db,
    get_all_homeworks_db,
)

homework_router = APIRouter(prefix='/homework', tags=['Homework'])



@homework_router.get('/get-all-homeworks')
async def get_all_homeworks():

    return get_all_homeworks_db()



# Get exact homework by ID
@homework_router.get('/exact-homework{id}')
async def get_exact_homework_DataBase(homework_id: int,):
    result = get_exact_homework(homework_id=homework_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Учитель не найден'}


# Add new homework
@homework_router.post('/add-homework')
async def add_new_homework(data: AddNewHomeworkValidator):

    homework_id = data.homework_id
    mark = data.mark
    homework_published_date = data.homework_published_date
    homework_deadline = data.homework_deadline
    subject = data.subject
    title = data.title
    description = data.description



    result = add_new_homework_db(homework_id,mark,homework_published_date,homework_deadline ,subject, title, description)

    return {'message': result}



# Edit homework info
@homework_router.put('/edit-homework')
async def edit_homework_info(homework_id: int,new_description,new_title):
    result = edit_homework_info_db(homework_id, new_description, new_title)

    return result


# Delete homework
@homework_router.delete('/delete-homework[id]')
async def delete_homework(homework_id: int):
    result = delete_homework_db(homework_id)

    if result:
        return {'message': f'Success {result}'}
    else:
        return {'message': 'Нету такого карты('}
