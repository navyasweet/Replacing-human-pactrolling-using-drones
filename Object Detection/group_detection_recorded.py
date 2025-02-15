import cv2
import numpy as np
import tensorflow as tf
import argparse
import sys
import time
import csv
import os 
IM_WIDTH = 640
IM_HEIGHT = 480


camera_type = 'usb'
parser = argparse.ArgumentParser()
parser.add_argument('--usbcam', help='Use a USB webcam instead of picamera', action='store_true')
parser.add_argument('--video', help='Name of the video file', default='test.mp4')
args = parser.parse_args()
if args.usbcam:
    camera_type = 'usb'
VIDEO_NAME = args.video

# Import utilites
from models.research.object_detection.utils import label_map_util
from models.research.object_detection.utils import visualization_utils as vis_util


MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH, 'models', 'research', 'object_detection', 'ssdlite_mobilenet_v2_coco_2018_05_09', 'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH, 'models', 'research', 'object_detection', 'data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.compat.v1.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

output = []

# Initialize the USB webcam
video = cv2.VideoCapture(0)  # 0 represents the default camera

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1280, 720))

# creating a fucntion 
def group_counting():
    
    # Initialize frame rate calculation
    frame_rate_calc = 1
    freq = cv2.getTickFrequency()
    font = cv2.FONT_HERSHEY_SIMPLEX

    while(video.isOpened()): # Uncomment block for recorded video input
    # Acquire frame and resize to expected shape [1xHxWx3]
    # Start timer (for calculating frame rate)
        t1 = cv2.getTickCount()
    
        ret, frame1 = video.read()
        if not ret:
            print('Reached the end of the video!')
            break

    
        frame = frame1.copy()
        frame.setflags(write=1)
        frame_expanded = np.expand_dims(frame, axis=0)

        
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: frame_expanded})


        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=4,
            min_score_thresh=0.45)
        
        
        Validobj = [category_index.get(value) for index, value in enumerate (classes[0]) if scores [0,index]>0.4]
        
        # Choose your object
        to_detect = 'person' 
        
        
        if Validobj:
            data = [i["name"] for i in Validobj]
            
            if data.count(to_detect)>1:
                
                Summary = ["Atleast " + str(data.count(to_detect)) + " people detected"]
                print(Summary, time.ctime())
                
                evidence_stamp = [data.count(to_detect),to_detect,time.ctime()]
                output.append(evidence_stamp)
                cv2.putText(frame,"ALERT: {}".format(Summary),(30,85),font,1,(60,60,255),2,cv2.LINE_AA)

                
        
        cv2.putText(frame,"FPS: {0:.2f}".format(frame_rate_calc),(30,50),font,1,(255,255,0),2,cv2.LINE_AA)

        vidout = cv2.resize(frame,(1280,720))
        out.write(vidout)

        
        cv2.imshow('Object detector', frame)

        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc = 1/time1
 
        if cv2.waitKey(1) == ord('q'):
            
            with open('output.csv','w',newline = '\n') as file:
                writer = csv.writer(file)
                writer.writerows(output)
            break

    cv2.destroyAllWindows()
    video.release() 
    out.release() 

try:
    while True:
        group_counting()
except KeyboardInterrupt:
    sys.exit()
