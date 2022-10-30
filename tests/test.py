#!/usr/bin/python3


import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	"""test for the class"""

	def setUp(self):
		self.my_model = BaseModel()

	def testforInstance(self):
		"""To check if my_model is an instance of Basemodel"""
		self.assertIsInstance(self.my_model, BaseModel)

	def testforId(self):
		"""To check if the id generated is as it should be"""
		self.assertRegex(self.my_model.id, '([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})')
	def testForCreated_at(self):
        	""" To check if the time is ISO format and it is valid time """
        	self.assertRegex(self.my_model.created_at, 'datetime.datetime([0-9]{4}, [0-9]{2}, [0-9]{2}, [0-9]{2}, [0-9]{2}, [0-9]{6})')

if __name__	 == "__main__":
	unittest.main()
