import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

database_name = 'fundraising'
database_user = os.getenv('DBUSER')
database_pw = os.getenv('DBPW')
database_host = os.getenv('DBHOST')
database_path = "postgresql+psycopg2://{}:{}@{}/{}".format(database_user, database_pw, database_host, database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Money_pot(db.Model):
    __tablename__ = 'money_pots'

    id = Column(Integer, primary_key=True)
    Title = Column(String)
    Description = Column(String)
    Target = Column(Integer)
    Pledge_total = Column(Integer)
    Status = Column(String)
