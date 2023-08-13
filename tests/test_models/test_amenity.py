#!/usr/bin/python3
""" Amenity Testing """
import unittest
import pep8
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Check the Amenity class """

    def test_pep8(self):
        """ Test code style using PEP8 """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])  # Check the code style
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

