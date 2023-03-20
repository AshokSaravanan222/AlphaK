import unittest
import imutils

import score
import numpy as np


class TestScore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image = imutils.read_image('test_images/image15.png')
        cls.yes = 121  # keyboard code for 'y'
        cls.no = 110  # keyboard code for 'n'

    def test_find_score_box(self):
        image = score.find_score_box(self.image)
        self.assertEqual(imutils.display(image, "identity"), self.yes)

        with self.subTest("Find Score Boxes"):
            score_boxes = score.find_all_boxes(image)
            image = np.copy(image)
            for box in score_boxes:
                imutils.draw_box(box, image)
            self.assertEqual(imutils.display(image, "score_boxes"), self.yes)


if __name__ == '__main__':
    unittest.main()
