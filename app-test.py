from urllib.parse import urlencode
from falcon import testing
import unittest
import json

import app

headers = {"Content-Type": "application/x-www-form-urlencoded"}


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        self.app = app.create()

    def tearDown(self):
        super(MyTestCase, self).tearDown()


class TestMyApp(MyTestCase):
    def test_empty_request_body(self):
        """Test empty body"""
        body = urlencode({})

        errorObject = {
            "error": "Bad request",
            "field_errors": {
                "first_name": ["This is required"],
                "last_name": ["This is required"],
                "email": ["This is required"],
                "password": ["This is required"]
            }
        }

        result = self.simulate_post(
            '/', body=body, headers=headers)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json, errorObject)

    def test_missing_fields(self):
        """Test missing fields"""
        body = json.dumps({"password": "ilovek@ndA"})

        errorObject = {
            "error": "Bad request",
            "field_errors": {
                "first_name": ["This is required"],
                "last_name": ["This is required"],
                "email": ["This is required"],
            }
        }

        result = self.simulate_post('/', body=body, headers=headers)

        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json, errorObject)

    def test_incorrect_type(self):
        """Test incorrect type for first name"""
        body = json.dumps({
            "first_name": 200,
            "last_name": "Holmes",
            "email": "sherlock@example.com",
            "password": "ilovek@ndA!"
        })

        errorObject = {
            "error": "Bad request",
            "field_errors": {
                "first_name": ["Invalid field type"]
            }
        }

        result = self.simulate_post('/', body=body, headers=headers)

        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json, errorObject)

    def test_invalid_password(self):
        """Test invalid password"""
        body = json.dumps({
            "first_name": "Sherlock",
            "last_name": "Holmes",
            "email": "sherlock@example.com",
            "password": "a"
        })

        errorObject = {
            "error": "Bad request",
            "field_errors": {
                "password": ["Password must at least be 8 characters"]
            }
        }

        result = self.simulate_post('/', body=body, headers=headers)

        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json, errorObject)

    def test_invalid_email(self):
        """Test invalid email"""
        body = json.dumps({
            "first_name": "Sherlock",
            "last_name": "Holmes",
            "email": "a@b.c",
            "password": "ilovek@ndA!"
        })

        errorObject = {
            "error": "Bad request",
            "field_errors": {
                "email": ["Invalid email format"]
            }
        }

        result = self.simulate_post('/', body=body, headers=headers)

        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json, errorObject)

    def test_valid_request(self):
        body = json.dumps({
            "first_name": "Sherlock",
            "last_name": "Holmes",
            "email": "sherlock@example.com",
            "password": "ilovek@ndA!"
        })

        data = {}

        result = self.simulate_post('/', body=body, headers=headers)
        print(result)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json, data)


if __name__ == '__main__':
    unittest.main()
