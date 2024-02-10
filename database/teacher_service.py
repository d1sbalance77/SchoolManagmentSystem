from database.models import Teacher
from database import get_db



def get_all_teachers_db():
    db = next(get_db())

    all_teachers = db.query(Teacher).all()

    return {"status": 1, "message": all_teachers}


def get_exact_teacher_info(teacher_id):
    db = next(get_db())

    exact_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if exact_teacher:
        return {'message': exact_teacher}
    else:
        return 'This Teacher does not exists in DataBase'


def get_exact_teacher_subject(teacher_id):
    db = next(get_db())

    exact_teacher_subject = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if exact_teacher_subject:
        return exact_teacher_subject.teacher_subject
    else:
        return 'This Teacher does not exists in DataBase'


def add_new_teacher_db(name, surname, phone_number, email, expirience, teacher_subject, salary):
    db = next(get_db())

    checker = db.query(Teacher).filter_by(phone_number=phone_number).first()

    if checker:
        return 'This phone number already registered'

    else:
        new_teacher = Teacher(name=name,
                        surname=surname,
                        phone_number=phone_number,
                        email=email,
                        expirience=expirience,
                        salary=salary,
                        teacher_subject=teacher_subject,
                            )


    db.add(new_teacher)
    db.commit()

    return 'New teacher was successfully registered'


# def login_user_db(phone_number, password):
#     db = next(get_db())
#
#     checker = db.query(User).filter_by(phone_number=phone_number,password=password).first()
#
#     if checker:
#         if checker.password == password:
#             return checker
#         elif checker.password != password:
#             return 'Incorrect password'
#     else:
#         return 'Error in data'



def edit_teacher_info_db(teacher_id,edit_info,new_info):
    db = next(get_db())

    exact_teacher = get_exact_teacher_info(teacher_id)

    if exact_teacher:
        if edit_info == 'name':
            exact_teacher.name = new_info

        elif edit_info == 'surname':
            exact_teacher.surname = new_info

        elif edit_info == 'expirience':
            exact_teacher.expirience = new_info

        elif edit_info == 'subject':
            exact_teacher.teacher_subject = new_info

        db.commit()

        return 'Infromation about a teacher was successfully edited'
    else:
        return "Infromation about a teacher was not successfully edited"



def delete_teacher_db(teacher_id):
    db = next(get_db())

    teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if teacher:

        db.delete(teacher)
        db.commit()

        return 'Teacher was successfully deleted'
    else:
        return 'Teacher was not successfully deleted'

