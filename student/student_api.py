from fastapi import APIRouter, HTTPException
from student import (
    AddNewStudentValidator,
    DeleteStudentValidator,
    EditStudentInfoValidator,
    # GetAllStudentsValidator,
    GetExactStudentValidator,
)
from database.student_service import (
    get_all_students_db,
    get_exact_student,
    add_new_student_db,
    edit_student_info_db,
    delete_student_db,
)

student_router = APIRouter(prefix='/student', tags=['Student'])

# Get all students
@student_router.get('/get-all-students')
async def get_all_students():

    return get_all_students_db()

# Get exact student by ID
@student_router.get('/exact-student/{student_id}')
async def get_exact_student_db(student_id: int):
    result = get_exact_student(student_id=student_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Учитель не найден'}

# Add new student
@student_router.post('/add-student')
async def add_new_student(data: AddNewStudentValidator):

    result = add_new_student_db(data.student_id,
                                data.name,
                                data.surname,
                                data.phone_number,
                                data.email,
                                data.city,
                                data.birthday)

    return {'message': result}


# Edit student info
@student_router.put('/edit-student/{student_id}', response_model=int)
async def edit_student_info(student_id: int , data: EditStudentInfoValidator):
    result = edit_student_info_db(student_id , data.edit_info, data.new_info)

    return result

@student_router.delete('/delete-student/student_id')
async def delete_student(student_id: int):
    result = delete_student_db(student_id)

    return result
