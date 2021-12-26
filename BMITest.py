"""
Created on 18 Dec 2021

@author: Anusha
"""

from calculateBMI import CalculateBMI
import unittest

class BMI_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Called once before any tests in class')

    @classmethod
    def tearDownClass(cls):
        print('Called once after all tests in class')

    def setUp(self):
        print('Called once befor each test in class')
        input = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        self.bmi = CalculateBMI(input)

    ## called end of test
    def tearDown(self):
        print("Done!!")

    def test_calbmi(self):   
        li = self.bmi.calBMI()
        self.assertTrue(len(li)>0)

    def test_countOverweight(self):
        count = self.bmi.countOverweight()
        self.assertTrue(count>0)
