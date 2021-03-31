import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Enable debug mode and silence notifications.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database
# database_name = 'fundraising'
# database_user = os.getenv('DBUSER')
# database_pw = os.getenv('DBPW')
# database_host = os.getenv('DBHOST')
# database_path = "postgresql+psycopg2://{}:{}@{}/{}".format(database_user, database_pw, database_host, database_name)
# SQLALCHEMY_DATABASE_URI = database_path

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

