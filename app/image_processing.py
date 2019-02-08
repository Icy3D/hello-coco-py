import cv2
from app.model import Model


class ImageProcessing:

    def __init__(self, model: Model):
        self._model = model
        self._rows = -1
        self._cols = -1
        self._capture = None
        self._img_output = None

    def create_capture(self):
        # cap = cv2.VideoCapture(0)
        self._capture = cv2.VideoCapture(self._model.capture_input)

    def get_next_frame(self):
        # Capture frame-by-frame
        ret, img_input = self._capture.read()
        if img_input is None:
            return None

        img_rectified = img_input.copy()

        if self._model.is_undistortion_active:
            self._model.camera.undistort(img_input, img_rectified)

        self._img_output = cv2.resize(img_rectified, (1280, 720))

        self._rows = self._img_output.shape[0]
        self._cols = self._img_output.shape[1]
        # inp = cv2.resize(imgLow, (300, 300))
        tf_input = self._img_output
        tf_input = tf_input[:, :, [2, 1, 0]]  # BGR2RGB
        return tf_input

    def detect(self, tf_result):
        # Visualize detected bounding boxes.
        num_detections = int(tf_result[0][0])

        for i in range(num_detections):
            class_id = int(tf_result[3][0][i])
            score = float(tf_result[1][0][i])
            bbox = [float(v) for v in tf_result[2][0][i]]

            if score > self._model.obj_det_thresh:
                x = bbox[1] * self._cols
                y = bbox[0] * self._rows
                right = bbox[3] * self._cols
                bottom = bbox[2] * self._rows
                pos = (int(x), int(y))
                color = self._model.label_colors[class_id - 1]

                cv2.rectangle(self._img_output, pos, (int(right), int(bottom)), color, 2)

                # setLabel('class: ' + str(classId), (int(x), int(y)))
                label = self._model.class_labels[class_id - 1] + ': ' + "{:.2f}".format(score)
                self.__draw_label(self._img_output, label, pos, color)
        return self._img_output

    def stop(self):
        self._capture.release()

    @staticmethod
    def __draw_label(img, text, pos, bg_color):
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.4
        color = (0, 0, 0)
        thickness = cv2.FILLED
        margin = 2

        txt_size = cv2.getTextSize(text, font_face, scale, thickness)

        end_x = pos[0] + txt_size[0][0] + margin
        end_y = pos[1] - txt_size[0][1] - margin

        cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
        cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)
