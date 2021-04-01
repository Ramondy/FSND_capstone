# FSND_capstone: "Fund My Fun" -- a Backend API to raise money from friends, family and fools 

## Getting Started

The application is deployed to Heroku with a ready-to-use PostgreSQL database for the duration of the
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
- permissions: post:money_pot, get:money_pot-details, patch:money_pot, delete:money_pot

### {user.name: Contributor, user.id: 2}
- permissions: get:user-details, post:pledge

## User Stories
- a Fundraiser creates a Money_pot to raise money
- a Fundraiser updates or deletes a Money_pot at will

- the list of all Money_pots is accessible to both Fundraisers and Contributors
- a Fundraiser can get details of all pledges for a Money_pot (get_money_pot_details)
- a Contributor pledges money to any Money_pot
- a Contributor can get details of his pledges

## Endpoints
- POST '/money_pots'
- GET '/money_pots'
- GET '/money_pots/<int:money_pot_id>'
- PATCH '/money_pots/<int:money_pot_id>'
- DELETE '/money_pots/<int:money_pot_id>'
- POST '/pledges'
- GET '/users/<int:user_id>'

#### POST '/money_pots'
- Creates a new Money Pot
- Request Arguments:
  {"title":string,
  "description":string,
  "target":integer, "owner_id":"1"}
#### GET '/money_pots'


#### GET '/money_pots/<int:money_pot_id>'


#### PATCH '/money_pots/<int:money_pot_id>'


#### DELETE '/money_pots/<int:money_pot_id>'


#### POST '/pledges'


#### GET '/users/<int:user_id>'
