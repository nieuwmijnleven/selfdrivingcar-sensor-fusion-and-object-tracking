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
#### (1) Extended Kalman Filter
* We implemented the functions of system matrix F, process noise covariance Q, prediction, and update states
* We introduced nonlinear function h(x) and applied to our kalman filter successfully.

#### (2) Track Management
* We introduce some confident values to assign them to a track
  * Track score
  * Track state
    * confirmed, tentative, initialized
* We implemented the following functions
  * Initialization of new tracks 
  * Update of the state and score of a track
  * Deletion of old tracks

#### (3) Data Association
* We implemented the following functions
  * Simple Nearest Neighbor(SNN)
  * Mahalanobis Distance(MHD)
  * Gating

#### (4) Camera-Lidar Sensor Fusion
* We implemented the following functions
  * Transformation from sensor coordinates to vehicle coordinates
  * Transformation from vehicle coordinates to sensor coordinates
  * Projection of a 3d point or a 6d state vector to 2d image space
    * nonlinear measurement function
  * Extended Kalman Filter 

### 2. Which results did you achieve? 
* We made an object tracking system using the extended kalman filter and sensor fusion
  * our object tracking system based on sensor fusion show us better precision than an object tracking system using lidar only   

### 3. Which part of the project was most difficult for you to complete, and why?
* It is challenging to understand and implement the Extended Kalman Filter. Some mathematical knowledge are need for understanding. For example, linear algebra, probabilities, statistics and differential equations. I managed to understand the Extended Kalman Filter and implement it.

### 4. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?
* Yes
  * Comparing the result of step 3 and step 4, step 4 which uses fusion system show better performance than step 3 which only uses lidar. 

### 5. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?
* Extracting meaningful data from a wide range of sensors in varying implementations, any of which potentially add device error, noise, and flaws in the data gathering process.
* Lack of performance under real-life conditions
* Power consumption

### 6. Can you think of ways to improve your tracking results in the future?
* Improving our model to consider accelerations
* Changing the association algorithm from Simple Nearest Neighbor(SNN) to Global Nearest Neighbor(GNN) or Joint Probabilistic Data Association(JPDA).
