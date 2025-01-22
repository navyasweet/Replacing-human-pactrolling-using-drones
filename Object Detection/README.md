## Object Detection

# Overview

This project implements object detection using TensorFlow and OpenCV. It utilizes the SSDLite MobileNet v2 COCO model to detect objects in real-time from a USB webcam or a video file. The program identifies multiple objects and counts the number of people detected in the frame. The detection results are displayed on the screen and saved in an output video file (output.avi). Additionally, a CSV file (output.csv) logs the detected objects and their timestamps.

# Files
```
group_detection_recorded.py - Main script for running object detection from a video or live webcam.

output.avi - Processed video output with detected objects highlighted.

output.csv - Log file containing detected object counts and timestamps.

sample.py - Sample script (if applicable) for testing or additional functionality.

```

# Requirements
```
Python 3.x

TensorFlow 2.x (with compatibility for TensorFlow 1.x methods)

OpenCV

NumPy

```

# Installation

* Clone the repository or download the project files.

* Install the required dependencies by running:

* pip install tensorflow opencv-python numpy

* Ensure the TensorFlow model is downloaded and placed correctly in the project directory:
```
models/research/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09
```
# Usage

Running the Object Detection Script

* Using a USB Camera (Default)
```
python group_detection_recorded.py --usbcam
```
* Running on a Video File
```
python group_detection_recorded.py --video test.mp4
```
# How It Works

* The script loads the SSDLite MobileNet v2 pre-trained model and the COCO dataset labels.

* The video stream is initialized from a USB camera or a video file.

* The object detection model processes each frame and identifies objects based on confidence thresholds.

* If more than one person is detected, an alert message appears on the screen.

* The processed frames are displayed in real-time and saved in output.avi.

* Detected object data, including timestamps, is logged in output.csv.

* The script runs until manually terminated (press 'q' to quit).

# Output

Live detection video with bounding boxes and labels.

output.avi: Video file containing the detection results.

output.csv: Log file storing detected object data and timestamps.

# Sample  Output 

![Screenshot 2023-10-04 151153](https://github.com/navyasweet/Live-Object-Detection-OPENCV-/assets/134292286/e598f687-b571-46df-adbc-84d1039d42b6)
![Screenshot 2024-01-03 220110](https://github.com/navyasweet/Live-Object-Detection-OPENCV-/assets/134292286/4705d108-a4ce-4000-bfc1-34984d2f3a47)



