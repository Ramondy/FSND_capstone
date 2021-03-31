import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
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

    # TEST MONEY_POTS ENDPOINTS

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

    def test_get_money_pots(self):
        res = self.client().get('/money_pots')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['money_pots'])

    def test_get_money_pot_details(self):
        id = self.test_post_money_pot()
        res = self.client().get('/money_pots/' + str(id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['money_pot_id'], id)

    def test_404_get_money_pot_details(self):
        res = self.client().get('/money_pots/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Resource not found.')

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

    def test_patch_money_pot(self):
        id = self.test_post_money_pot()
        res = self.client().patch('/money_pots/' + str(id), json={"description": "This is the new description."})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['money_pot_id'], id)

    def test_404_patch_money_pot(self):
        res = self.client().patch('/money_pots/1000', json={"description": "This is the new description."})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Resource not found.')

    # TEST PLEDGES ENDPOINTS
    def test_post_pledge(self):
        res = self.client().post('/pledges', json={"user_id": "2", "money_pot_id": "1", "amount": "10"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['pledge_id'])

    def test_400_post_pledge(self):
        res = self.client().post('/pledges', json={"user_id": None, "money_pot_id": None, "amount": "10"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'Bad request.')

    # TEST USERS ENDPOINTS
    def test_get_user_details(self):
        res = self.client().get('/users/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['user_details'])

    def test_404_get_user_details(self):
        res = self.client().get('/users/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'Resource not found.')

if __name__ == "__main__":
    unittest.main()