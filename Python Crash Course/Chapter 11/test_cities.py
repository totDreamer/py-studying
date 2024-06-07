from city_functions import city_functions
import unittest

class CitiesTest(unittest.TestCase):
    """Tests for city functions."""
    def test_city_country(self):
        """Is the return value correct?"""
        ret_val = city_functions('Verkhotyrye', 'Russia')
        self.assertEqual(ret_val, 'Verkhotyrye, Russia')

    def test_city_name_population(self):
        """Is the return value with population correct?"""
        ret_val = city_functions('Verkhotyrye', 'Russia', population='10 000')
        self.assertEqual(ret_val, 'Verkhotyrye, Russia - population 10 000')

if __name__ == '__main__':
    unittest.main()