from db import get_db, close_db


def expand_payment(payment):
    db = get_db()
    result = db.execute(
        'SELECT * FROM persons WHERE id IN (SELECT payee_id FROM payees WHERE payment_id  = ?)',
        (payment.get('id'),)
    )
    payment['payees'] = [dict(payee) for payee in result]
    result = db.execute(
        'SELECT * FROM persons WHERE id = ?',
        (payment.get('payer_id'),)
    )
    payment['payer'] = dict(result.fetchone())


def get_payments():
    db = get_db()
    result = db.execute('SELECT * FROM payments')
    payments = [dict(payment) for payment in result]
    for payment in payments:
        expand_payment(payment)
    close_db()
    return payments


def post_payment(description, amount, payer_id, payee_ids):
    db = get_db()
    cursor = db.cursor()
    result = cursor.execute(
        'INSERT INTO payments(description, amount, payer_id) VALUES(?,?,?)',
        (
            description,
            amount,
            payer_id
        )
    )
    payment_id = cursor.lastrowid
    print('PAYMENT_ID: ' + str(payment_id))
    for payee_id in payee_ids:
        db.execute(
            'INSERT INTO payees(payee_id,payment_id) VALUES(?,?)',
            (
                payee_id,
                payment_id
            )
        )
    db.commit()
    close_db()


def delete_payments():
    db = get_db()
    db.execute('DELETE FROM payees')
    db.execute('DELETE FROM payments')
    db.commit()
    close_db()


def get_payment(payment_id):
    db = get_db()
    result = db.execute('SELECT * FROM payments WHERE id = ?', (payment_id,))
    payment = dict(result.fetchone())
    expand_payment(payment)
    close_db()


def delete_payment(payment_id):
    db = get_db()
    db.execute('DELETE FROM payees WHERE payment_id = ?', (payment_id,))
    db.execute('DELETE FROM payments WHERE id = ?', (payment_id,))
    db.commit()
    close_db()
