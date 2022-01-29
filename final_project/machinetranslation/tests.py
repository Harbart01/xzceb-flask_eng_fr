import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_to_french('How are you'), 'comment vas-tu')
        self.assertNotEqual(english_to_french('Good night'), 'Bonsoir') 
        self.assertIsNone(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Ma maison'), 'My house')
        self.assertNotEqual(french_to_english('donnez-moi ce sac'), 'give me my shoe')
        self.assertIsNone(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()