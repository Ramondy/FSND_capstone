# FSND_capstone: "Fund My Fun" -- a Backend API to raise money from friends, family and fools 

## Getting Started

The application is deployed to Heroku with a ready-to-use PostgreSQL database for the duration of the
FSND capstone project assessment at the following url: https://fundmyfun.herokuapp.com/

## Stack
- Flask, SQLAlchemy
- PostgreSQL
- Auth0
- Heroku

## Instructions for Local Deployment
### Dependencies
This project uses Python 3.7. You can install dependencies by running the following command from the project root:
```bash
pip install -r requirements.txt
```

### Database Setup
You will need to create a PostgreSQL database.

Then you will create a .env file at the root, where you can assign the full path to your database to the following environment variable:
DATABASE_URL

### Authentication using Auth0

0) Create an App and an API in your Auth0 account.


1) Add the following environment variables to the .env file with the values you gather from Auth0: 
AUTH0_DOMAIN, AUTH0_client_ID, AUTH0_client_secret, API_AUDIENCE


2) Create two roles (Fundraiser, Contributor) and at least one user for each role. 

   
3) The Fundraiser should have the following permissions: post:money_pot, get:money_pot-details, patch:money_pot, delete:money_pot


4) The Contributor should have the following permissions: get:user-details, post:pledge


5) Login each user to Auth0 to get back their JWT, which you will then save as environment variables: JWT_Fundraiser, JWT_Contributor


6) Insert User data in the database, using the psql command line. For instance:

```bash
INSERT INTO users (name, email) VALUES ('Fundraiser', 'email_1@email.com');
INSERT INTO users (name, email) VALUES ('Contributor', 'email_2@email.com');
```
7) Take note of the user ID assigned in the database to the Fundraiser and Contributor, which you will need as parameter for some endpoints.

## User types

There are two types of users : Fundraisers and Contributors. Fundraisers manage Money_pots,
Contributors pledge money to Money_pots. 
The production db on Heroku already contains one user of each type:

- {user.id: 1, user.name: Fundraiser}
- {user.id: 2, user.name: Contributor}


## User Stories
- a Fundraiser creates a Money_pot to raise money
- a Fundraiser updates or deletes a Money_pot at will

- the list of all Money_pots is accessible to both Fundraisers and Contributors
- a Fundraiser can get details of all pledges for a Money_pot (get_money_pot_details)
- a Contributor pledges money to any Money_pot
- a Contributor can get details of his pledges

## Endpoints

Note: temporarily valid JWTs and examples for curl requests are provided in examples.txt
- POST '/money_pots'
- GET '/money_pots'
- GET '/money_pots/<int:money_pot_id>'
- PATCH '/money_pots/<int:money_pot_id>'
- DELETE '/money_pots/<int:money_pot_id>'
- POST '/pledges'
- GET '/users/<int:user_id>'

#### POST '/money_pots'
- Creates a new money_pot
- Request Arguments:
  {"title":string, "description":string, "target":integer, "owner_id":"1"}
- Returns: an object with one key
  {'money_pot_id': id of the item created}

#### GET '/money_pots'
- Fetches the list of all money_pots
- Request Arguments: None
- Returns: a list of dict:
  {"id": int, "owner_id": int, "pledge_total": int, "status": str, "target": int, "title": str}

#### GET '/money_pots/<int:money_pot_id>'
- Fetches the details on a particular money_pot
- Request Arguments: <int:money_pot_id>
- Returns: an object with two keys
  {"money pot": a dict containing money_pot information (see GET '/money_pots'),
  "pledges": a list of dict, containing pledge information (see GET '/users/<int:user_id>')}

#### PATCH '/money_pots/<int:money_pot_id>'
- Updates a particular money_pot
- Request Arguments: <int:money_pot_id>, a dict containing new data
- Returns: an object with one key
  {'money_pot_id': id of the item updated}

#### DELETE '/money_pots/<int:money_pot_id>'
- Deletes a particular money_pot and all related pledges
- Request Arguments: <int:money_pot_id>
- Returns: an object with one key
  {'money_pot_id': id of the item deleted}

#### POST '/pledges'
- Creates a new pledge
- Request Arguments:
  {"user_id": int, "money_pot_id": int, "amount": int}
- Returns: an object with one key
  {'pledge_id': id of the item created}

#### GET '/users/<int:user_id>'
- Fetches the list of all pledges for a user
- Request Arguments: <int:user_id>
- Returns: an object with two keys
  {"user_id": user_id,
  "pledges": a list of dict, containing pledge information
   {"amount": int, "pledge_id": int, "money_pot_id": int, "user_id": int}
  