from database.models import Homework
from database import get_db

# getting all homeworks
def get_all_homeworks_db():
    db = next(get_db())

    all_homeworks = db.query(Homework).all()

    return {'status': 1, 'message': all_homeworks}


# Getting exact homework by id
def get_exact_homework(homework_id):
    db = next(get_db())

    exact_homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if exact_homework:
        return exact_homework
    else:
        return 'This Homework does not exists in DataBase'


# Addinf new homework
def add_new_homework_db(homework_id,mark,homework_published_date, homework_deadline,subject,title,description):
    db = next(get_db())

    checker = db.query(Homework).filter_by(homework_id=homework_id).first()

    if checker:
        return 'This Homework was already registered'

    else:
        new_homework = Homework(homework_id=homework_id,
                                mark=mark,
                                homework_published_date=homework_published_date,
                                homework_deadline=homework_deadline,
                                subject=subject,
                                title=title,
                                description=description)


    db.add(new_homework)
    db.commit()

    return 'New homework was successfully added'


# Edit homework info
def edit_homework_info_db(homework_id, new_subject,new_title):
    db = next(get_db())

    exact_homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if exact_homework:
        exact_homework.subject = new_subject
        exact_homework.title = new_title

        db.commit()

        return 'Successfully edited'
    else:
        return "Student not found"



# Deleting Homework
def delete_homework_db(homework_id):
    db = next(get_db())

    homework = db.query(Homework).filter_by(homework_id=homework_id).first()

    if homework:
        db.delete(homework)
        db.commit()

        return 'Homework was successfully deleted'
    else:
        return 'Homework was not successfully deleted'

