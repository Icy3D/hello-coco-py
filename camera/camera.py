import cv2
from camera.camera_matrix import CameraMatrix
from camera.distortion_coefficients import DistortionCoefficients


class Camera:

    def __init__(self, width=1980, height=1080, fov_x=90.0, fov_y=50.625):
        self._width = width
        self._height = height
        self._cm = CameraMatrix(self._width, self._height, fov_x, fov_y)
        self._dc = DistortionCoefficients()

    def undistort(self, src, dst):
        cm = self._cm.matrix()
        dc = self._dc.matrix()
        cv2.undistort(src, cm, dc, dst)

    @property
    def camera_matrix(self):
        return self._cm

    @camera_matrix.setter
    def camera_matrix(self, value):
        self._cm = value

    @property
    def distortion_coefficients(self):
        return self._dc

    @distortion_coefficients.setter
    def distortion_coefficients(self, value):
        pass

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

