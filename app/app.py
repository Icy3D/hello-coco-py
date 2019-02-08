import tensorflow as tf

from app.gui import Gui
from app.image_processing import ImageProcessing
from app.model import Model
from camera.camera import Camera


class App:

    def __init__(self):
        self._model = Model()
        self._gui = Gui(self._model)
        self._ip = ImageProcessing(self._model)
        self._tf_session = None

    def set_coco_data(self, graph_definitions_file, class_labels_file):
        self._model.load_coco_data(graph_definitions_file, class_labels_file)

    def set_capture_input(self, filename_or_hardware_id, camera_type: Camera):
        self._model.set_capture_input(filename_or_hardware_id, camera_type)

    def run(self):
        self._tf_session = tf.Session()

        # Restore session
        self._tf_session.graph.as_default()
        tf.import_graph_def(self._model.graph_definitions, name='')

        self._ip.create_capture()
        self._gui.create_ui_elements()
        self.loop()

        self._ip.stop()
        self._gui.stop()

    def loop(self):
        while True:

            # read the next camera frame
            img_input = self._ip.get_next_frame()
            if img_input is None:
                break

            # setup tensorflow parameters
            num = self._tf_session.graph.get_tensor_by_name('num_detections:0')
            scores = self._tf_session.graph.get_tensor_by_name('detection_scores:0')
            boxes = self._tf_session.graph.get_tensor_by_name('detection_boxes:0')
            classes = self._tf_session.graph.get_tensor_by_name('detection_classes:0')
            feed_dict = {'image_tensor:0': img_input.reshape(1, img_input.shape[0], img_input.shape[1], 3)}
            # Run the tensorflow/coco model
            tf_result = self._tf_session.run([num, scores, boxes, classes], feed_dict)

            # draw the tf results into the output image and display it
            img_output = self._ip.render_detection(tf_result)
            cancel = not self._gui.show_image(img_output)

            if cancel:
                break

    def __is_ready(self):
        return True
