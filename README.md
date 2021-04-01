# FSND_capstone: "Fund My Fun" -- a Backend API to raise money from friends, family and fools 

## Getting Started

The application is deployed to Heroku together with a ready-to-use PostgreSQL database for the duration of the
FSND capstone project assessment at the following url: https://fundmyfun.herokuapp.com/

## Stack
- Flask, SQLAlchemy
- PostgreSQL
- Auth0
- Heroku

## User types

There are two types of users : Fundraisers and Contributors. Fundraisers manage Money_pots,
Contributors pledge money to Money_pots. 
The production db already contains one user of each type:
### {user.name: Fundraiser, user.id: 1}
role: Fundraiser |
user_email: dhihpmqp@sharklasers.com |
permissions: post:money_pot, get:money_pot-details, patch:money_pot, delete:money_pot

### {user.name: Contributor, user.id: 2}
role: Contributor | 
user_email: lcufnlul@sharklasers.com |
permissions: get:user-details, post:pledge

## User Stories
- a Fundraiser creates a Money_pot to raise money
- a Fundraiser updates or deletes a Money_pot at will

- the list of all Money_pots is accessible to both Fundraisers and Contributors
- a Fundraiser can get details of all pledges for a Money_pot (get_money_pot_details)
- a Contributor pledges money to any Money_pot
- a Contributor can get details of his pledges

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

curl -X GET https://fundmyfun.herokuapp.com/users