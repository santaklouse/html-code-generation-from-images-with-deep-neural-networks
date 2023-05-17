__author__ = 'Taneem Jan, taneemishere.github.io'

import numpy as np


class Utils:
    @staticmethod
    def sparsify(label_vector, output_size):
        sparse_vector = []

        for label in label_vector:
            sparse_label = np.zeros(output_size)
            sparse_label[label] = 1

            sparse_vector.append(sparse_label)

        return np.array(sparse_vector)

    @staticmethod
    def get_preprocessed_img(img_path, image_size):
        import cv2
        # from keras.preprocessing.image import array_to_img, img_to_array
        # img = array_to_img(img_path)
        # img = img_to_array(img)
        # img = cv2.imread(img_path)
        # don't need to read the image as we're now directly passing the 
        # image as numpy array to this method
        img = cv2.resize(img_path, (image_size, image_size))
        img = img.astype('float32')
        img /= 255
        return img

    @staticmethod
    def show(image):
        import cv2
        cv2.namedWindow("view", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("view", image)
        cv2.waitKey(0)
        cv2.destroyWindow("view")
