import unittest
from color_myworld_app import MyPerson


class PersonNameTests(unittest.TestCase):
    def test_name_person(self):
        first_person = MyPerson("Karee")
        result = first_person.name
        self.assertEqual('Karee', result)