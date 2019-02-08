import cv2
from app.model import Model


class Gui:

    # hack for the trackbar callback
    # opencv can only deal with static callback methods, hence this reference to the instance
    self = None

    def __init__(self, model: Model):
        self._slider_max = 1000
        self._model = model
        Gui.self = self

    def create_ui_elements(self):
        cv2.namedWindow(self._model.win_parameters_title)
        cv2.resizeWindow(self._model.win_parameters_title, 600, 350)

        dc = self._model.camera.distortion_coefficients

        self.create_trackbar('Detection thresh', 0.0, 1.0, self._model.obj_det_thresh, Gui.on_trackbar_obj_det_thresh)
        self.create_trackbar('Lense k1', -0.5, 0.5, dc.k1, Gui.on_trackbar_k1)
        self.create_trackbar('Lense k2', -0.02, 0.02, dc.k2, Gui.on_trackbar_k2)
        self.create_trackbar('Lense p1', -1.0, 1.0, dc.p1, Gui.on_trackbar_p1)
        self.create_trackbar('Lense p2', -1.0, 1.0, dc.p2, Gui.on_trackbar_p2)
        self.create_trackbar('Lense k3', -0.002, 0.002, dc.k3, Gui.on_trackbar_k3)

    def create_trackbar(self, title, min_val, max_val, slider_val, callback):
        cv2.createTrackbar(title,
                           self._model.win_parameters_title,
                           self.value_to_slider(min_val, max_val, slider_val),
                           self._slider_max,
                           callback)

    def slider_to_value(self, min_val, max_val, slider_val):
        perc = slider_val / float(self._slider_max)
        val_range = max_val - min_val
        val = min_val + perc * val_range
        return float(val)

    def value_to_slider(self, min_val, max_val, val):
        val_range = max_val - min_val
        perc = (val - min_val) / val_range
        slider_val = self._slider_max * perc
        return int(slider_val)

    def render(self, img_output):
        cv2.imshow("Result - press space to toggle lens distortion", img_output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            return False
        elif key == ord(' '):
            self._model.toggle_undistortion()
            return True

    # opencv can only deal with static callback methods, hence this static method
    @staticmethod
    def on_trackbar_obj_det_thresh(slider_val):
        Gui.self._model.obj_det_thresh = Gui.self.slider_to_value(0.0, 1.0, slider_val)
        print('thresh: ' + str(Gui.self._model.obj_det_thresh))

    def on_trackbar_k1(slider_val):
        Gui.self._model.camera.distortion_coefficients.k1 = Gui.self.slider_to_value(-0.5, 0.5, slider_val)
        print('k1: ' + str(Gui.self._model.camera.distortion_coefficients.k1))

    def on_trackbar_k2(slider_val):
        Gui.self._model.camera.distortion_coefficients.k2 = Gui.self.slider_to_value(-0.02, 0.02, slider_val)
        print('k2: ' + str(Gui.self._model.camera.distortion_coefficients.k2))

    def on_trackbar_k3(slider_val):
        # convert to -1.0 to 1.0
        Gui.self._model.camera.distortion_coefficients.k3 = Gui.self.slider_to_value(-0.002, 0.002, slider_val)
        print('k3: ' + str(Gui.self._model.camera.distortion_coefficients.k3))

    def on_trackbar_p1(slider_val):
        result = Gui.self.slider_to_value(-1.0, 1.0, slider_val)
        Gui.self._model.camera.distortion_coefficients.p1 = result
        print('p1: ' + str(result))

    def on_trackbar_p2(slider_val):
        # convert to -1.0 to 1.0
        Gui.self._model.camera.distortion_coefficients.p2 = Gui.self.slider_to_value(-1.0, 1.0, slider_val)
        print('p2: ' + str(Gui.self._model.camera.distortion_coefficients.p2))

    @staticmethod
    def stop():
        cv2.destroyAllWindows()
