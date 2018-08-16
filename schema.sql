CREATE TABLE persons (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL
);

CREATE TABLE payments (
id INTEGER PRIMARY KEY,
description VARCHAR(255) NOT NULL,
amount REAL NOT NULL,
payer_id INTEGER NOT NULL,
FOREIGN KEY(payer_id) REFERENCES persons(id)
);

CREATE TABLE payees (
payee_id INTEGER NOT NULL,
payment_id INTEGER NOT NULL,
FOREIGN KEY(payee_id) REFERENCES persons(id),
FOREIGN KEY(payment_id) REFERENCES payments(id)
);
