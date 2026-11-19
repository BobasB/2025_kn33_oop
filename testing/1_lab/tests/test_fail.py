import unittest

class TestFail(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2)  # This test is designed to fail