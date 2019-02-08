import cv2
from camera import camera_matrix
from camera import distortion_coefficients


class Camera:

    def __init__(self):
        self._cm = camera_matrix.CameraMatrix()
        self._dc = distortion_coefficients.DistortionCoefficients()

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

