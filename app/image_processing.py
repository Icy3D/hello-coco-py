import cv2
from app.model import Model
from app.rendertools import RenderTools as rt


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
        cam = self._model.camera

        if self._model.is_undistortion_active:
            cam.undistort(img_input, img_rectified)

        img720 = self.rescale720(cam, img_rectified)
        img32size = self.get_image_size_32(img720)
        self._img_output = self.letterbox_image(img720, img32size)

        self._rows = self._img_output.shape[0]
        self._cols = self._img_output.shape[1]
        # inp = cv2.resize(imgLow, (300, 300))
        tf_input = self._img_output
        tf_input = tf_input[:, :, [2, 1, 0]]  # BGR2RGB
        return tf_input

    def get_image_size_32(self, img720):
        # resize the image to something 32x32
        h, w, c = img720.shape
        x32 = w - (w % 32)
        y32 = h - (h % 32)
        img32size = (x32, y32)
        return img32size

    def rescale720(self, cam, img_rectified):
        # # rescaling - limiting video size to 720p
        target_height = 720
        target_width = int(target_height * (float(cam.width) / float(cam.height)))
        img720 = cv2.resize(img_rectified, (target_width, target_height))
        return img720

    def render_detection(self, image, tf_result):
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
                rt.draw_label(self._img_output, label, pos, color)
        return self._img_output

    def stop(self):
        self._capture.release()



    @staticmethod
    def letterbox_image(image, size):
        '''resize image with unchanged aspect ratio using padding'''
        ih, iw, c = image.shape
        w, h = size
        scale = min(w / iw, h / ih)
        nw = int(iw * scale)
        nh = int(ih * scale)

        result = cv2.resize(image, (nw, nh))
        # image = image.resize((nw, nh), Image.BICUBIC)
        # new_image = Image.new('RGB', size, (128, 128, 128))
        # new_image.paste(image, ((w - nw) // 2, (h - nh) // 2))
        return result
