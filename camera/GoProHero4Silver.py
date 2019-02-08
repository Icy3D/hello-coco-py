from camera import camera


# see
# http://argus.web.unc.edu/camera-calibration-database/
# https://gopro.com/help/articles/Question_Answer/HERO4-Field-of-View-FOV-Information


class GoProHero4Silver(camera.Camera):

    def __init__(self, width=1920, height=1080, fov_x=118.2, fov_y=69.5):
        super().__init__()

        cm = self.camera_matrix
        cm.cx = width / 2.0
        cm.cy = height / 2.0
        cm.fx_from_fov(fov_x, width)
        cm.fy_from_fov(fov_y, height)

        dc = self.distortion_coefficients
        # dc.k1 = -0.31
        # dc.k2 = 0.17
        # dc.t1 = 0.0
        # dc.t2 = 0.0
        # dc.k3 = 0.0

        dc.k1 = -0.11
        dc.k2 = 0.01644
        dc.p1 = 0.0
        dc.p2 = 0.0
        dc.k3 = -0.001368
