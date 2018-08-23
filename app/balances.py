from persons import get_persons
from payments import get_payments


def calculate_balances():
    persons = get_persons()
    payments = get_payments()

    balances = dict()
    for person in persons:
        person_id = person.get('id')
        name = person.get('name')
        balances[person_id] = {'id': person_id, 'balance': 0.0, 'name': name}

    for payment in payments:
        payer_id = payment.get('payer').get('id')
        payee_ids = [payee.get('id') for payee in payment.get('payees')]
        amount = payment.get('amount')

        balances[payer_id]['balance'] += amount
        for payee_id in payee_ids:
            balances[payee_id]['balance'] -= amount / len(payee_ids)
            
    return [balance for key,balance in balances.items()]


def resolve_transactions():
    balances = calculate_balances()
    transactions = []

    for balance in balances:
        if (balance['balance'] < 0):
            for other_balance in balances:
                if other_balance['balance'] > 0 and balance['balance'] < 0:
                    amount = min(-balance['balance'], other_balance['balance'])
                    transactions.append({
                        'from': balance['name'],
                        'to': other_balance['name'],
                        'amount': amount
                    })
                    balance['balance'] += amount
                    other_balance['balance'] -= amount

    return transactions
