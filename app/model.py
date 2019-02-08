from camera.gopro_hero4_silver import GoProHero4Silver
from app.tools import Tools
from camera.camera import Camera
import tensorflow as tf


class Model:

    def __init__(self):
        self.camera = None
        self.class_labels = None
        self.obj_det_thresh = 0.5
        self.label_colors = None
        self.capture_input = None
        self.graph_definitions = None
        self.class_labels = None
        self.is_undistortion_active = True
        self.win_parameters_title = 'Parameters'
        self.win_image_title = 'Result - press space to toggle lens undistortion'

    def set_capture_input(self, capture_input, camera: Camera):
        self.capture_input = capture_input
        self.camera = camera

    def load_coco_data(self, graph_definitions_file, class_labels_file):
        try:
            self.__load_graph_definitions(graph_definitions_file)
            self.__load_class_labels(class_labels_file)
            self.label_colors = Tools.create_colors(len(self.class_labels))
            return True
        except:
            return False

    def toggle_undistortion(self):
        self.is_undistortion_active = not self.is_undistortion_active

    def __load_graph_definitions(self, model_file):
        with tf.gfile.FastGFile(model_file, 'rb') as f:
            self.graph_definitions = tf.GraphDef()
            self.graph_definitions.ParseFromString(f.read())

    def __load_class_labels(self, class_labels_file):
        with open(class_labels_file) as f:
            self.class_labels = f.read().split('\n')
