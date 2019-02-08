from app.app import App
from camera.gopro_hero4_silver import GoProHero4Silver
from camera.camera import Camera

videos = ['videos/busstation.mp4', 'videos/india.mp4', 'videos/crosswalk.mp4']
input_video = videos[0]

# provide the video resolution and if available the horizontal (fov_x) and vertical (fov_y) field of view
cam = Camera(1280, 720)

# in case you have your own video and/or want to do some specific lens corrections
# input_video = 'videos/volley1.mp4'
# cam = GoProHero4Silver()

# in case you have a webcam you want to do something like this
# input_video = 0
# cam = Camera(960, 720, 90.0, 67.5)

class_list = 'models/classid.txt'
graph_definitions = 'models/frozen_inference_graph_ssdlite.pb'
# graph_definitions = 'models/frozen_inference_graph_mrcnn.pb'

app = App()
app.set_coco_data(graph_definitions, class_list)
app.set_capture_input(input_video, cam)
app.run()
