from tokenize import String
import unittest
from generateCSV import PersonalData


class TestPersonalData(unittest.TestCase):

    def test_patient(self):
        self.assertMultiLineEqual(PersonalData.patient(), String, msg="Deu ruim")

    """def test_age(self):
        for i in range(11, 95):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
    
    def test_gender(self):
        self.assertMultiLineEqual('', '')
"""
unittest.main()
