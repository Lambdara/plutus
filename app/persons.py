from db import get_db, close_db

def get_persons():
    db = get_db()
    db_result = db.execute('SELECT * FROM persons')
    persons = [dict(schedule) for schedule in db_result]
    close_db()
    return persons


def post_person(name):
    db = get_db()
    db.execute('INSERT INTO persons(name) VALUES(?)',(name,))
    db.commit()
    close_db()


def delete_persons():
    db = get_db()
    db.execute('DELETE FROM persons')
    db.commit()
    close_db()


def get_person(person_id):
    db = get_db()
    result = db.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
    person = dict(result.fetchone())
    close_db()
    return person


def delete_person(person_id):
    db = get_db()
    db.execute('DELETE FROM persons WHERE id = ?', (person_id,))
    db.commit()
    close_db()
