import unittest

from cancer_prediction.cancer_model import CancerModel


class TestCancerModel(unittest.TestCase):

    def test_diagnosis_to_target(self):
        model = CancerModel()
        diagnosis = "Benign"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 1)

        diagnosis = "Malignant"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 0)

    def test_target_to_diagnosis(self):
        model = CancerModel()
        target2 = 1
        diagnosis2 = model.target_to_diagnosis(target2)
        self.assertEqual(diagnosis2, "Benign")

        target2 = 0
        diagnosis2 = model.target_to_diagnosis(target2)
        self.assertEqual(diagnosis2, "Malignant")


if __name__ == "__main__":
    unittest.main()
