import unittest
import color_myworld_app

class PersonNameTests(unittest.TestCase):
    def test_name_person(self):
        person=Person()
        result=person.name('Alicia')
        self.assertEqual('Alicia',result)
        print result