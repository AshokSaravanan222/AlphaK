import unittest
import image_methods

import identity


class TestIdentity(unittest.TestCase):

    image = image_methods.read_image('test_images/image10.png')

    yes = 121  # keyboard code for 'y'
    no = 110  # keyboard code for 'n'

    def test_find_identity_box(self):
        image = identity.find_identity_box(self.image)
        self.assertEqual(image_methods.display(image), self.yes)

    def test_find_subject_box(self):
        image = identity.find_subject_box(self.image)
        self.assertEqual(image_methods.display(image), self.yes)

    def test_find_name_box(self):
        self.assertEqual(True, True)  # add assertion here

    def test_find_student_id_box(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
