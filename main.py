from app.app import App
from camera.GoProHero4Silver import GoProHero4Silver
import os


graph_definitions = 'models/frozen_inference_graph_ssdlite.pb'
class_list = 'models/classid.txt'
input_video = 'videos/busstation.mp4'
cam = GoProHero4Silver()

app = App()
app.set_coco_data(graph_definitions, class_list)
app.set_capture_input(input_video, cam)
app.run()
