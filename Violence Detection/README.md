# Violence Detection

# Overview

This project implements a real-time Violence Detection System using TensorFlow and OpenCV. The system processes video frames to detect violent actions and raises an alert if violence is detected. If an incident occurs, it logs the event and records the relevant footage.

# Table of Contents
```
violence-detection/
│-- localfile-testing.ipynb  # Jupyter notebook for local file testing
│-- mamonbest947oscombo-drive.hdfs  # Pretrained model weight file
│-- mamonbest947oscombo.h5  # Model weight file
│-- mamonfight22.py  # Python script containing the violence detection model
│-- predicting-localvideo.py  # Script for processing local videos
│-- README.md  # Project documentation
```
# Installation

>  Prerequisites

Ensure you have Python 3.x installed. Then, install the required dependencies:
``
pip install tensorflow numpy scikit-image opencv-python
``
> Usage

1: Running Real-Time Detection

2: To start violence detection using your webcam, run:
``
python mamonfight22.py
``
3: Running Detection on a Local Video File

4: To detect violence in a pre-recorded video file:
``
6ython predicting-localvideo.py --video your_video.mp4
``
5: The model used is mamon_videoFightModel2, which loads pre-trained weights from mamonbest947oscombo.h5.

5: The detection system processes 30 frames at a time with a resolution of 160x160.

7: If violence is detected with an accuracy of 96% or more, an alert message is displayed and the footage is saved.

# Output

> Real-Time Detection: Displays the live video stream with violence alerts.
![voilence](https://github.com/user-attachments/assets/f214d27f-37ce-41fc-b96a-9ae8197cd94e)

> Recorded Video: Captured footage is saved in ./videos/output-<index>.avi.

> Console Logs: Prints messages when violence is detected.

# Potential Improvements

* Improve accuracy by training with additional datasets.
* Optimize frame processing for better performance.
* Implement real-time alert notifications via email or SMS.
* Integrate a web-based dashboard for monitoring and alerts.
