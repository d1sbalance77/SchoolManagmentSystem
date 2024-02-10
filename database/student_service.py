from database.models import Student
from database import get_db


def get_all_students_db():
    db = next(get_db())

    all_students = db.query(Student).all()

    return {'status': 1, 'message': all_students}


def get_exact_student(student_id):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    if exact_student:
        return exact_student
    else:
        return 'This Student does not exists in DataBase'


def add_new_student_db(student_id, name, surname, phone_number, email, city, birthday):
    db = next(get_db())

    checker = db.query(Student).filter_by(phone_number=phone_number).first()

    if checker:
        return 'New Student was successfully registered'
    else:
        new_student = Student(student_id=student_id,
                        name=name,
                        surname=surname,
                        phone_number=phone_number,
                        email=email,
                        city=city,
                        birthday=birthday)



    db.add(new_student)
    db.commit()

    return 'New Student successfully registered'


def edit_student_info_db(student_id, new_name, new_birthday):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    if exact_student:
        exact_student.name = new_name
        exact_student.birthday = new_birthday

        db.commit()

        return 'Successfully edited'
    else:
        return "Student not found"


def delete_student_db(student_id):
    db = next(get_db())

    student = db.query(Student).filter_by(student_id=student_id).first()

    if student:

        db.delete(student)
        db.commit()

        return 'Student was successfully deleted'
    else:
        return 'Student was not successfully deleted'

