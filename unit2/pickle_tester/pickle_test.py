import unittest
from pickler import list_pickler, unpickler

class PickleTest(unittest.TestCase):
    def test_list_pickle_unpickle_the_same(self):
        self.my_list=['a','b','c']
        list_pickler(self.my_list)
        unpickled_list=unpickler(self.my_list)
        self.assertEqual(self.my_list,unpickled_list)

