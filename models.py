# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import os
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import Column, String, Integer

from dotenv import load_dotenv

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
load_dotenv()
database_name = 'fundraising'
database_user = os.getenv('DBUSER')
database_pw = os.getenv('DBPW')
database_host = os.getenv('DBHOST')
database_path = "postgresql+psycopg2://{}:{}@{}/{}".format(database_user, database_pw, database_host, database_name)


app = Flask(__name__)
moment = Moment(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class User(db.Model):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    email = Column(db.String)

    # RELATIONSHIPS
    money_pots = db.relationship('MoneyPot', backref='owner')


class MoneyPot(db.Model):
    __tablename__ = 'money_pots'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    target = Column(Integer)
    pledge_total = Column(Integer)
    status = Column(String)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
