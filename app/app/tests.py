from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test Add Function"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test Subtract Function"""
        self.assertEqual(subtract(12, 2), 10)
