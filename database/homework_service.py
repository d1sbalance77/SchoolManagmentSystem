from datetime import datetime
from database.models import Homework
from database import get_db


def get_all_homeworks_db():
    db = next(get_db())

    all_homeworks = db.query(Homework).all()

    return {'status': 1, 'message': all_homeworks}



def get_exact_homework(homework_id):
    db = next(get_db())

    exact_homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if exact_homework:
        return exact_homework
    else:
        return 'This Homework does not exists in DataBase'


def add_new_homework_db(homework_id,subject,title,description,homework_deadline):
    db = next(get_db())

    checker = db.query(Homework).filter_by(homework_id=homework_id).first()

    if checker:
        return 'This Homework was already registered'

    else:
        new_homework = Homework(subject=subject,
                                title=title,
                                description=description,
                                homework_deadline=homework_deadline,
                               )

    db.add(new_homework)
    db.commit()

    return 'New homework was successfully added'



def edit_homework_info_db(homework_id, edit_info, new_info):
    db = next(get_db())

    exact_homework = get_exact_homework(homework_id)

    if exact_homework:
        if edit_info == 'title':
            exact_homework.title = new_info

        elif edit_info == 'description':
            exact_homework.description = new_info

        elif edit_info == 'homework_deadline':
            exact_homework.homework_deadline = new_info

        db.commit()

        return 'Homework details was successfully edited'
    else:
        return "Homework details was not successfully edited"


def delete_homework_db(homework_id):
    db = next(get_db())

    homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if homework:
        db.delete(homework)
        db.commit()

        return 'Homework was successfully deleted'
    else:
        return 'Homework was not successfully deleted'

