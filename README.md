# Final Project: Sensor Fusion and Object Tracking

## STEP1
```
$> python loop_over_dataset_STEP1.py
```
### (1) Visualization
<kbd>
 <img src = "img/report/step1_animation.gif?raw=true" width=1000 />
</kbd>

### (2) Experimental Results
<kbd>
 <img src = "img/report/step1.png?raw=true" width=1000 />
</kbd>

## STEP2
```
$> python loop_over_dataset_STEP2.py
```
### (1) Visualization
<kbd>
 <img src = "img/report/step2_animation.gif?raw=true" width=1000 />
</kbd>

### (2) Experimental Results
<kbd>
 <img src = "img/report/step2.png?raw=true" width=1000 />
</kbd>

## STEP3
```
$> python loop_over_dataset_STEP3.py
```
### (1) Visualization
<kbd>
 <img src = "img/report/step3_animation.gif?raw=true" width=1000 />
</kbd>

### (2) Experimental Results
<kbd>
 <img src = "img/report/step3.png?raw=true" width=1000 />
</kbd>

## STEP4
```
$> python loop_over_dataset_STEP4.py
```
### (1) Visualization
<kbd>
 <img src = "img/report/step4_animation.gif?raw=true" width=1000 />
</kbd>

### (2) Experimental Results
<kbd>
 <img src = "img/report/step4.png?raw=true" width=1000 />
</kbd>

## Writeup Instructions

### 1. Write a short recap of the four tracking steps and what you implemented there (EKF, track management, data association, camera-lidar sensor fusion). 
* (1) Extended Kalman Filter
 * We implemented the functions of system matrix F, process noise covariance Q, prediction, and update states
 * We introduced nonlinear function h(x) and applied to our kalman filter successfully.
* Track Management
* Data Association
* Camera-Lidar Sensor Fusion

### (2) Which results did you achieve? Which part of the project was most difficult for you to complete, and why?
### (3) Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?
### (4) Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?
### (5) Can you think of ways to improve your tracking results in the future?

