from camera import camera
from camera.camera_matrix import CameraMatrix


# see
# http://argus.web.unc.edu/camera-calibration-database/
# https://gopro.com/help/articles/Question_Answer/HERO4-Field-of-View-FOV-Information


class GoProHero4Silver(camera.Camera):

    def __init__(self, width=1920, height=1080, fov_x=118.2, fov_y=69.5):
        super().__init__(width, height, fov_x, fov_y)

        dc = self.distortion_coefficients
        dc.k1 = -0.11
        dc.k2 = 0.01644
        dc.p1 = 0.0
        dc.p2 = 0.0
        dc.k3 = -0.001368
