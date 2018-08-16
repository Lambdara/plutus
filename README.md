# Plutus

Plutus keeps financial balance in a group

Plutus implements a REST-API and provides a web-interface to easily access it.

## API specification

| Path                     | Modes             | Description       |
| ------------------------ | ----------------- | ----------------- |
| `/persons/`              | GET, POST, DELETE | Index of persons  |
| `/persons/<PERSON_ID>`   | GET, DELETE       | Person object     |
| `/payments/`             | GET, POST, DELETE | Index of payments |
| `/payments/<PAYMENT_ID>` | GET, DELETE       | Payment object    |

## Dependencies

- Flask
