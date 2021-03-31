# FSND_capstone: "Fund My Fun" -- a web app to raise money from friends, family and fools 

https://fundmyfun.herokuapp.com/
https://git.heroku.com/fundmyfun.git
DATABASE_URL: postgres://irfswhdcwujhtd:118bc1b5d9d359a303458d6f4072d1344bce899394f8ba4c5e73c70b8f9bbbf1@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d8pmnceds530km


## Stack
- Flask, PSQL, SQLAlchemy
- Auth0
- Docker, Heroku

## Use Cases

There are two types of users : Fundraisers and Contributors. Fundraisers create Money_pots,
Contributors pledge money to Money_pots. 

DONE, TESTED - a Fundraiser creates a Money_pot to raise money
DONE, TESTED - a Fundraiser updates or deletes a Money_pot at will

DONE, TESTED - the list of all Money_pots is accessible to both Fundraisers and Contributors
DONE, TESTED - a Fundraiser can get details of all pledges for a Money_pot (get_money_pot_details)
DONE, TESTED - a Contributor pledges money to any Money_pot
DONE, TESTED - a Contributor can get details of his pledges


## Auth0 User IDs
API: FSND

role: Contributor | 
user_email: lcufnlul@sharklasers.com |
user_pw: lcufnlul |
permissions: get:money_pot, post:pledge, delete:pledge

role: Fundraiser |
user_email: dhihpmqp@sharklasers.com |
user_pw: dhihpmqp |
permissions: post:money_pot, patch:money_pot, get:money_pot-details, delete:money_pot, 

## Models
- Money_pot:
- Pledge:
- User

## tests

curl -X GET http://127.0.0.1:8080/users
curl -X GET http://127.0.0.1:8080/money_pots

POST MONEY_POT:
curl -X POST http://127.0.0.1:8080/money_pots -H "Content-Type: application/json" -d '{"title":"second money_pot", "description":"This is the second one.", "target":"100", "owner_id":"1"}'
curl -X POST http://127.0.0.1:8080/money_pots -H "Content-Type: application/json" -d '{"title":"third money_pot", "description":"No need.", "owner_id":"1"}'

POST PLEDGE:
curl -X POST http://127.0.0.1:8080/pledges -H "Content-Type: application/json" -d '{"user_id":"2", "money_pot_id":"1", "amount":"10"}'

PATCH MONEY_POT:
curl -X PATCH http://127.0.0.1:8080/money_pots/2 -H "Content-Type: application/json" -d '{"description":"This is the new description."}'
curl -X PATCH http://127.0.0.1:8080/money_pots/2 -H "Content-Type: application/json" -d '{"status":"closed"}'

DELETE MONEY_POT:
curl -X DELETE http://127.0.0.1:8080/money_pots/3 -H "Content-Type: application/json"