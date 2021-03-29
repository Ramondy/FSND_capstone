# FSND_capstone: "Fund My Fun" -- a web app to raise money from friends, family and fools 

## Stack
- Flask, PSQL, SQLAlchemy
- Auth0
- Docker, Heroku

## Use Cases

There are two types of users : Fundraisers and Contributors. Fundraisers create Money_pots,
Contributors pledge money to Money_pots. 

- a Fundraiser creates a Money_pot to raise money
- a Fundraiser updates, closes or deletes a Money_pot at will

- the list of all open Money_pots is accessible to both Fundraisers and Contributors
- a User pledges money to any Money_pot
- pledges are anonymous except to the Fundraiser

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

curl -X GET http://127.0.0.1:8080/users
curl -X GET http://127.0.0.1:8080/money_pots

POST MONEY_POT:
curl -X POST http://127.0.0.1:8080/money_pots -H "Content-Type: application/json" -d '{"title":"second money_pot", "description":"This is the second one.", "target":"100", "owner_id":"1"}'

POST PLEDGE:
curl -X POST http://127.0.0.1:8080/pledges -H "Content-Type: application/json" -d '{"user_id":"2", "money_pot_id":"1", "amount":"10"}'

