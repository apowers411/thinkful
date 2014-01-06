import unittest
from color_myworld_app import MyPerson


class PersonNameTests(unittest.TestCase):
    def test_name_person(self):
        first_person = MyPerson("Karee")
        result = first_person.name
        self.assertEqual('Karee', result)

    def test_setBio(self):
        first_person=MyPerson("Karee")
        result = first_person.setBio("My name is Karee")
        self.assertEqual("My name is Karee",first_person.bio)

#if writing to a database more tests
