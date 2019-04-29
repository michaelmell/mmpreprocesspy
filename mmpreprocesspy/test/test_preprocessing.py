from unittest import TestCase
import skimage.transform
import matplotlib.pyplot as plt
import mmpreprocesspy.dev_auxiliary_functions as dev_aux


class TestPreprocessing(TestCase):
    test_data_base_path = '/home/micha/Documents/git/MM_Testing'

    def test_find_main_channel_orientation__returns_angle_0__for_main_channel_in_vertical_direction(self):
        from mmpreprocesspy import preprocessing

        image_array = read_tiff_to_nparray(
            self.test_data_base_path + '/04_20180531_gluIPTG5uM_lac_1/first_images/Pos0/04_img_000000000_ DIA Ph3 (GFP)_000.tif')

        angle = preprocessing.find_main_channel_orientation(image_array)

        self.assertEqual(0, angle)

    def test_find_main_channel_orientation__returns_angle_90__for_main_channel_in_horizontal_direction(self):
        from mmpreprocesspy import preprocessing

        image_array = read_tiff_to_nparray(
            self.test_data_base_path + '/04_20180531_gluIPTG5uM_lac_1/first_images/Pos0/04_img_000000000_ DIA Ph3 (GFP)_000.tif')
        image_array = skimage.transform.rotate(image_array, 90)

        angle = preprocessing.find_main_channel_orientation(image_array)

        self.assertEqual(90, angle)

    def test_create_growthlane_objects(self):
        from mmpreprocesspy import preprocessing

        regions = preprocessing.get_growthlane_regions([1, 2], 20, 20)
        pass

    def test_get_transformation_matrix(self):
        from mmpreprocesspy import preprocessing
        import cv2 as cv

        image_array = read_tiff_to_nparray(
            self.test_data_base_path + '/04_20180531_gluIPTG5uM_lac_1/first_images/Pos0/04_img_000000000_ DIA Ph3 (GFP)_000.tif')

        horizontal_shift = 50
        vertical_shift = 100
        rotation_angle = -45
        rotation_center = (image_array.shape[1]/2 - 0.5, image_array.shape[0]/2 - 0.5)


        matrix = preprocessing.get_transformation_matrix(horizontal_shift, vertical_shift, rotation_angle, rotation_center)

        image_array = cv.warpAffine(image_array, matrix, (image_array.shape[1], image_array.shape[0]))

        dev_aux.show_image(image_array)


def read_tiff_to_nparray(image_path):
    """Reads tiff-image and returns it as a numpy-array."""

    from PIL import Image
    import numpy as np

    image_base = Image.open(image_path)
    return np.array(image_base, dtype=np.uint16)


    # @staticmethod
    # def show_image(image): # this method is currently broken
    #     image.mode = 'I'
    #     im2 = image.point(lambda i: i * (1. / 256)).convert('L')
    #     im2.show()

