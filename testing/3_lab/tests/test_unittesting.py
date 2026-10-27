from lab3.new import new_function, new_3, new_none
from lab3.main import main

import unittest

class TestNewFunction(unittest.TestCase):
    def test_new_function(self):
        result = new_function()
        self.assertIsInstance(result, str)
        self.assertIn("Повернене випадкове число:", result)

    def test_new_3(self):
        result = new_3()
        self.assertIsInstance(result, str)

    def test_new_none(self):
        result = new_none()
        self.assertIsNone(result)