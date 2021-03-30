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

    def test_post_money_pot(self):
        res = self.client().post('/money_pots', json={"title": "test create money_pot", "description": "This is a test.",
                                                      "target": "100", "owner_id": "1"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['money_pot_id'])

        return data['money_pot_id']

    def test_400_post_money_pot(self):
        res = self.client().post('/money_pots', json={"title": None, "description": "This is a failing test.",
                                                      "target": "100", "owner_id": None})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'Bad request.')

    def test_delete_money_pot(self):
        id = self.test_post_money_pot()
        res = self.client().delete('/money_pots/'+str(id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['money_pot_id'], id)

    def test_404_delete_money_pot(self):
        res = self.client().delete('/money_pots/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Resource not found.')


if __name__ == "__main__":
    unittest.main()