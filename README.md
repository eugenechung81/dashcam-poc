# Description 

This is a POC utilizing OpenCV, FastCV, and TLD.  

# Technologies 

OpenCV 
* real time computer vision libraries 
* written in C++, bindings available in python 
* motion understanding, hci, otion tracking, augmented realiity, machine learning support 

FastCV 
* better sdk / developed by qualcomms 
* focused on mobile devices (android first, works on ios/others)
* used by ionroad 
* high speed computation to identify shapes and field of view 

TLD
* algorithm tracking unknown ojects in unconstrained video streams
* tracks object and learns appearance, detects again when in appears in video 
* written in C++ 

# Installation 

* Follow instructions here: http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/
* Compile Fix: http://stackoverflow.com/questions/31663498/opencv-3-0-0-make-error-with-ffmpeg

# Grabbing Sample Videos 

1.  Use youtube-dl (e.g. Search: "dashcam", "security footage")
2.  Slice using VLC 

# Test 

```
python meanshift_test.py 
python camshift_test.py 
python motion_detector.py --video videos/robbery.mp4
```

# Results 

* Dashcam Meanshift: https://youtu.be/esotW6TFkFs
* Traffic Meanshift: https://youtu.be/NyR_7e7JXAA
* Robbery Motion Detection: https://youtu.be/nOdJ8osPdr4