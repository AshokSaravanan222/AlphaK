import unittest
import identity
import score
import cv2


class TestIdentity(unittest.TestCase):
    yes = 121  # keyboard code for 'y'
    no = 110  # keyboard code for 'n'

    def test_find_subject_box(self):
        image = cv2.imread('images/image13.png')
        self.assertEqual(identity.find_subject_box(image), self.yes)

    def test_find_name_box(self):
        self.assertEqual(True, True)  # add assertion here

    def test_find_student_id_box(self):
        self.assertEqual(True, True)  # add assertion here


class TestScore(unittest.TestCase):
    def test_find_score_boxes(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
