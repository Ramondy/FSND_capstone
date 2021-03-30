import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from main import create_app
from models import setup_db
from config import *


class FundMyFunTestCase(unittest.TestCase):
    """This class represents the FundMyFun api test case"""

    def setUp(self):
        """Executed before reach test"""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = database_name
        self.database_user = database_user
        self.database_pw = database_pw
        self.database_host = database_host
        self.database_path = database_path

        self.app.config.from_object('config')

        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_health(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()