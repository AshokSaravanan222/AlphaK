import unittest
import imutils

import identity


class TestIdentity(unittest.TestCase):

    image = imutils.read_image('test_images/image1.png')

    yes = 121  # keyboard code for 'y'
    no = 110  # keyboard code for 'n'

    # def test_find_page(self):
    #     image = identity.find_page(self.image)
    #     self.assertEqual(imutils.display(image, "page"), self.yes)

    def test_find_identity_box(self):
        image = identity.find_identity_box(self.image)
        self.assertEqual(imutils.display(image, "identity"), self.yes)

    def test_find_subject_box(self):
        image = identity.find_subject_box(self.image)
        self.assertEqual(imutils.display(image, "subject"), self.yes)

    def test_find_name_box(self):
        self.assertEqual(True, True)  # add assertion here

    def test_find_student_id_box(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
