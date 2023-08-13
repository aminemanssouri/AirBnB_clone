#!/usr/bin/python3
""" Testing Files """
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTesting(unittest.TestCase):
    """ Check BaseModel """

    def test_pep8(self):
        """ Test code style using PEP8 """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py',
                                         'models/__init__.py',
                                         'models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """ Test class for BaseModel """
    my_model = BaseModel()

    def tearDown(self):
        """ Delete json file """
        del self.test

    def setUp(self):
        """ Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """ Test None attribute """
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs_constructor_2(self):
        """ Check id with data """
        dictionary = {'score': 100}

        object_test = BaseModel(**dictionary)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))
        self.assertTrue(hasattr(object_test, 'score'))

    def test_str(self):
        """ Test string """
        dictionary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        object_test = BaseModel(**dictionary)
        out = "[{}] ({}) {}\n".format(type(object_test).__name__, object_test.id, object_test.__dict__)

    def test_to_dict(self):
        """ Check dictionary """
        object_test = BaseModel(score=300)
        new_dict = object_test.to_dict()

        self.assertEqual(new_dict['id'], object_test.id)
        self.assertEqual(new_dict['score'], 300)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['created_at'], object_test.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['updated_at']), str)

    def test_datetime(self):
        """ Check datetime """
        base1 = BaseModel()
        self.assertFalse(datetime.now() == base1.created_at)

    def test_base_model_attributes(self):
        """ Check attribute values in a BaseModel """

        self.my_model.name = "Holbie"
        self.my_model.my_number = 100
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def test_save_first(self):
        """ Check numbers """
        with self.assertRaises(AttributeError):
            BaseModel.save([455, 323232, 2323, 2323, 23332])

    def test_save_second(self):
        """ Check string """
        with self.assertRaises(AttributeError):
            BaseModel.save("THIS IS A TEST")

    def test_instance(self):
        """ Check class """
        ml = BaseModel()
        self.assertTrue(ml, BaseModel)  # Change comment and place of line but will still work

