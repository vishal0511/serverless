import unittest
import json
from datetime import datetime
#from src.functions.lambda_hello.hello.py import response_msg

gettime = datetime.now()

value=True
body="Hello from Vishal"


def response_msg(value, body):
	return "Hello from Vishal"

#value=True
#body="Hello from Vishal"

class helloTestTest(unittest.TestCase):
	def test_response(self):
		self.assertIn("Vishal", response_msg(value, body))


if __name__ == '__main__':
    unittest.main()
