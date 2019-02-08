import numpy as np
import cv2


class CameraMatrix:

    rad_to_degree = _rad_to_degree = np.pi / 180

    def __init__(self, width, height, fov_x, fov_y):
        self._fx = CameraMatrix.fov_to_pixel(fov_x, width)
        self._fy = CameraMatrix.fov_to_pixel(fov_y, height)
        self._cx = width / 2.0
        self._cy = height / 2.0

    # ATTENTION fov_y and fy are different values
    # see alphay here
    # https://github.com/opencv/opencv/blob/2.4/modules/calib3d/src/calibration.cpp#L1778
    @staticmethod
    def fov_to_pixel(fov, resolution):
        angle = CameraMatrix.rad_to_degree * fov / 2
        divisor = 2 * np.tan(angle)
        f_pixel = resolution / divisor
        return f_pixel

    def matrix(self):
        result = np.array([[self._fx, 0, self._cx],
                           [0, self._fy, self._cy],
                           [0, 0, 1]], np.float)
        return result

    @property
    def fx(self):
        return self._fx

    @fx.setter
    def fx(self, value):
        self._fx = value



    @property
    def fy(self):
        return self._fy

    @fy.setter
    def fy(self, value):
        self._fy = value

    def fov_y(self, value, height):
        # https://stackoverflow.com/questions/39992968/how-to-calculate-field-of-view-of-the-camera-from-camera-intrinsic-matrix
        # fov_y = 2 * np.arctan(height / 2 * self._fy)
        self._fy = height / (2 * np.tan(value / 2))

    @property
    def cx(self):
        return self._cx

    @cx.setter
    def cx(self, value):
        self._cx = value

    @property
    def cy(self):
        return self._cy

    @cy.setter
    def cy(self, value):
        self._cy = value
