# FSND_capstone: "Fund My Fun" -- a web app to raise money from friends, family and fools 

## Stack
- Flask, PSQL, SQLAlchemy
- Auth0
- Docker, Heroku

## Use Cases

There are two types of users : Fundraisers and Contributors. Fundraisers create Money_pots,
Contributors pledge money to Money_pots. 

- a Fundraiser creates a Money_pot to raise money
- a Fundraiser updates or deletes a Money_pot at will
- a Money_pot stays open until the target is reached or the Fundraiser deletes the Money_pot

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




