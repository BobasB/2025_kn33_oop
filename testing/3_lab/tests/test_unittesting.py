from lab3.new import new_function, new_3, new_none
from lab3.main import main
from lab3.branch import fun_with_if_else, fun_with_if_only

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

    def test_branches_positive(self):
        i = 5
        result = fun_with_if_else(i)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Positive")

    def test_branches_zero(self):
        i = 0
        result = fun_with_if_else(i)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Zero")


    def test_if_only_branch(self):
        # перевіряємо лише гілку if x > 0
        self.assertEqual(fun_with_if_only(5), "Positive")

    def test_if_only_branch_non_positive(self):
        # перевіряємо гілку if x <= 0
        self.assertEqual(fun_with_if_only(-3), "Non-positive")
        self.assertEqual(fun_with_if_only(0), "Non-positive")
