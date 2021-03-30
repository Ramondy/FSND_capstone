import os
import unittest
import json

from main import create_app

class FundMyFunTestCase(unittest.TestCase):
    """This class represents the FundMyFun api test case"""

    def setUp(self):
        """Executed before reach test"""
        self.app = create_app()
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

if __name__ == "__main__":
    unittest.main()