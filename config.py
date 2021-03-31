import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Connect to the database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

