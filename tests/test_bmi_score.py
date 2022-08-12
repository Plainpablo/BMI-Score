import unittest
from src.BMI_Score import bmi_score

class TestBmiScore(unittest.TestCase):

    def test_bmi(self):
        self.assertEqual(bmi_score.bmi(120, 30), 20.8)
        self.assertEqual(bmi_score.bmi(100, 50), 50.0)


    def test_bmi_information(self):
        self.assertEqual(bmi_score.bmi_information(12.0),"You're in the underweight range")
        self.assertEqual(bmi_score.bmi_information(18.0),"You're in the underweight range")
        self.assertEqual(bmi_score.bmi_information(19.0),"You're in the healthy weight range")
        self.assertEqual(bmi_score.bmi_information(20.5),"You're in the healthy weight range")
        self.assertEqual(bmi_score.bmi_information(25),"You're in the overweight range")
        self.assertEqual(bmi_score.bmi_information(29.4),"You're in the overweight range")
        self.assertEqual(bmi_score.bmi_information(30.0),"You're in the obese range")
        self.assertEqual(bmi_score.bmi_information(41.2),"You're in the obese range")



if __name__ == '__main__':
    unittest.main()