import unittest
import imutils
import numpy as np

import identity


class TestIdentity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.image = imutils.read_image('test_images/image1.png')
        cls.yes = 121  # keyboard code for 'y'
        cls.no = 110  # keyboard code for 'n'

    def test_find_identity_box(self):
        image = identity.find_identity_box(self.image)
        self.assertEqual(imutils.display(image, "identity"), self.yes)

        with self.subTest("Find All Boxes"):
            identity_boxes = identity.find_all_boxes(image)
            image = np.copy(image)
            for box in identity_boxes:
                imutils.draw_box(box, image)
            self.assertEqual(imutils.display(image, "all_boxes"), self.yes)

    def test_remove_boxes(self):
        image = identity.find_identity_box(self.image)
        identity_boxes = identity.find_all_boxes(image)
        with self.subTest("Remove Border Boxes"):
            indexes = identity.remove_border_boxes(image, identity_boxes)
            imutils.remove_indexes(indexes, image, identity_boxes)
            draw_image = np.copy(image)
            for box in identity_boxes:
                imutils.draw_box(box, draw_image)
            self.assertEqual(imutils.display(draw_image, "no border"), self.yes)
        with self.subTest("Remove Small Boxes"):
            indexes = identity.remove_small_boxes(identity_boxes)
            imutils.remove_indexes(indexes, image, identity_boxes)
            draw_image = np.copy(image)
            for box in identity_boxes:
                imutils.draw_box(box, draw_image)
            self.assertEqual(imutils.display(draw_image, "no small width"), self.yes)
        with self.subTest("Remove Kumon Logo"):
            indexes = identity.remove_logo(identity_boxes)
            imutils.remove_indexes(indexes, image, identity_boxes)
            draw_image = np.copy(image)
            for box in identity_boxes:
                imutils.draw_box(box, draw_image)
            self.assertEqual(imutils.display(draw_image, "no logo"), self.yes)

    # def test_find_subject_box(self):
    #     image = identity.find_subject_box(self.image)
    #     self.assertEqual(imutils.display(image, "subject"), self.yes)

    def test_find_name_box(self):
        self.assertEqual(True, True)  # add assertion here

    def test_find_student_id_box(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
