import unittest
import imutils

import identity


class TestIdentity(unittest.TestCase):

    image = imutils.read_image('test_images/image10.png')

    yes = 121  # keyboard code for 'y'
    no = 110  # keyboard code for 'n'

    def test_find_identity_box(self):
        image = identity.find_identity_box(self.image)
        self.assertEqual(imutils.display(image, "identity"), self.yes)

    def test_find_all_boxes(self):
        image = identity.find_identity_box(self.image)
        identity_boxes = identity.find_all_boxes(image)
        for box in identity_boxes:
            imutils.draw_box(box, image)
        self.assertEqual(imutils.display(image, "all_boxes"), self.yes)

    # def test_find_subject_box(self):
    #     image = identity.find_subject_box(self.image)
    #     self.assertEqual(imutils.display(image, "subject"), self.yes)

    def test_find_name_box(self):
        self.assertEqual(True, True)  # add assertion here

    def test_find_student_id_box(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
