#!/usr/bin/python3
""" Testing User """
import unittest
import pep8
from models.user import User

class UserTesting(unittest.TestCase):
    """ Test the User class """

    def test_pep8(self):
        """ Test code style using PEP8 """
        pep8_style = pep8.StyleGuide(quiet=True)
        file_path = 'models/user.py'
        result = pep8_style.check_files([file_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")  # Change comment and place of line but will still work

