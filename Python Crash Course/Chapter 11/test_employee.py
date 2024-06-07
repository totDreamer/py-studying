import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for Employee class."""

    def setUp(self):
        self.my_employee = Employee("Mikhail", "Bekker", 5500)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 10500)

    def test_give_unusual_raise(self):
        self.my_employee.give_raise(raise_value=7500)
        self.assertEqual(self.my_employee.salary, 13000)


if __name__ == '__main__':
    unittest.main()
