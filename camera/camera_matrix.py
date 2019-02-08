import numpy as np
import cv2


class CameraMatrix:

    def __init__(self):
        self._fx = 0.0
        self._fy = 0.0
        self._cx = 0.0
        self._cy = 0.0
        self._rad_to_degree = np.pi / 180

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

    # ATTENTION fov_x and fx are different values
    # see alphax here
    # https://github.com/opencv/opencv/blob/2.4/modules/calib3d/src/calibration.cpp#L1778
    def fx_from_fov(self, fov_x, width):
        # fov_x = 2 * np.arctan(width / (2 * self._fx))
        angle = self._rad_to_degree * fov_x / 2
        divisor = 2 * np.tan(angle)
        self._fx = width / divisor

    @property
    def fy(self):
        return self._fy

    @fy.setter
    def fy(self, value):
        self._fy = value

    # ATTENTION fov_y and fy are different values
    # see alphay here
    # https://github.com/opencv/opencv/blob/2.4/modules/calib3d/src/calibration.cpp#L1778
    def fy_from_fov(self, fov_y, height):
        angle = self._rad_to_degree * fov_y / 2
        divisor = 2 * np.tan(angle)
        self._fy = height / divisor

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
