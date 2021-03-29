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

    # ATTRIBUTES
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    email = Column(db.String)

    # RELATIONSHIPS
    money_pots = db.relationship('MoneyPot', backref='owner')

    # METHODS
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email  # ,'money_pots': self.money_pots
        }


class MoneyPot(db.Model):
    __tablename__ = 'money_pots'

    # ATTRIBUTES
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    target = Column(Integer)
    pledge_total = Column(Integer)
    status = Column(String)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # METHODS
    def __init__(self, title, description, target, owner_id):
        self.title = title
        self.description = description
        self.target = target
        self.pledge_total = 0
        self.status = 'open'
        self.owner_id = owner_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'target': self.target,
            'pledge_total': self.pledge_total,
            'status': self.status,
            'owner_id': self.owner_id
        }