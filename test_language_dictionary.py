import io
import unittest
from unittest.mock import patch
from language_dictionary import VerbDictionary

class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.object1 = VerbDictionary()
        verb_dictionary = {'müssen':'have to'}
        self.object2 = VerbDictionary(verb_dictionary)
        self.assertIsNotNone(self.object1.verb_dictionary)
        self.assertIsNotNone(self.object2.verb_dictionary)


    def test_read_from_textfile(self):
        self.object1.read_from_textfile('test_file.txt')
        self.object2.read_from_textfile()
        self.assertEqual(len(self.object1.verb_dictionary), 1) 
        self.assertEqual(len(self.object2.verb_dictionary), 100) 

        

    def test_find_meaning_in_dictionary(self):
        self.assertEqual(self.object1.find_meaning_in_dictionary('müssen'), 'have to')
        self.assertEqual(self.object2.find_meaning_in_dictionary('rockon'), 'NO MEANING FOUND')
        

if __name__ == '__main__':
    # a = VerbDictionary()
    # a.read_from_textfile('test_file.txt')
    # print(a.verb_dictionary)
    # print(a.find_meaning_in_dictionary('müssen'))
    unittest.main()