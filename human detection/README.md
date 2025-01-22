# Human Detection using OpenCV

# Description
This project uses OpenCV's HOG (Histogram of Oriented Gradients) descriptor to perform human detection in images, videos, and live camera feeds. It detects people and draws bounding boxes around them, displaying the total count of detected persons.

# Features:
* Detects people in images, videos, or real-time camera feed.
Draws bounding boxes around detected people.
* Detects people in images, videos, or real-time camera feed.
* Labels detected people as Person 1, Person 2, etc.
* Displays the total count of detected persons.
* Option to save the output to a video or image.
# Requirements
```
Python 3.x
OpenCV
imutils
pip install opencv-python imutils numpy
```

# How It Works:
> HOG Descriptor: The cv2.HOGDescriptor() is used to initialize the default people detector.
> Detection Process:The script captures frames from the video or webcam.
> For each frame, the HOGCV.detectMultiScale method detects people and draws bounding boxes around them.
> Output: The script displays the processed frame and, if specified, saves the output video or image to the given path.
> 
# How to Use
> Command-Line Arguments:
--video: Path to the video file for human detection.
--image: Path to the image file for human detection.
--camera: Set to true to use the webcam for live detection.
--output: Path to save the output video/image file (optional).

# Detecting people in an image:
> Using the webcam for real-time detection:
![human structure](https://github.com/user-attachments/assets/a0b28131-83fe-406a-b089-8e1caf7a5525)

# Sample Output Image:
![Screenshot 2023-10-04 151153](https://github.com/navyasweet/Live-Object-Detection-OPENCV-/assets/134292286/e598f687-b571-46df-adbc-84d1039d42b6)
Bounding boxes will be drawn around detected people.
Text displaying the status (Detecting) and total number of detected persons will be shown on the screen.
