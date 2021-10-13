# Mid-Term Project: 3D Object Detection

## ID_S1_EX1
```
$> python loop_over_dataset_ID_S1_EX1.py
```
<img src = "img/report/ID_S1_EX1.png?raw=true" width=1000 />
<img src = "img/report/ID_S1_EX1-2.png?raw=true" width=1000 />

## ID_S1_EX2
```
$> python loop_over_dataset_ID_S1_EX2.py
```
### Overall 3D Point Cloud
<img src = "img/report/ID_S1_EX2.png?raw=true" width=700 />

### Details of Overall 3D Point Cloud 
#### Find and display 6 examples of vehicles with varying degrees of visibility in the point-cloud
<img src = "img/report/ID_S1_EX2_DETAIL.png?raw=true" width=700 />

#### Identify vehicle features that appear as a stable feature on most vehicles (e.g. rear-bumper, tail-lights) and describe them briefly
* Lidar is located in the lower right of the image
* The closer the cars are to the Lidar sensor, The higher the resolution of the cars are
  * The car 1, 2, 5 and 6 which are close to the Lidar sensor are represented as high resolution images
    * we can see the cars as rectagles
    * we can recognize the front mirrors of the cars 
  * However, The car 7, 8, and 9 which are far away from the Lidar sensor are represented as low resolution images 
    * we cannot see the cars as rectagles
  * Moreover, some beams from the Lidar cannot reach to the car 3 and 4 as there are other cars in front of them

## ID_S2
```
$> python loop_over_dataset_ID_S2.py
```

### ID_S2_EX1
<img src = "img/report/ID_S2_EX1.png?raw=true" width=700 />

### ID_S2_EX2
<img src = "img/report/ID_S2_EX2.png?raw=true" width=700 />

### ID_S2_EX3
<img src = "img/report/ID_S2_EX3.png?raw=true" width=700 />

## ID_S3
```
$> python loop_over_dataset_ID_S3.py
```

### ID_S3_EX1
<img src = "img/report/ID_S3-EX1.png?raw=true" width=800 />

### ID_S3_EX2
<img src = "img/report/ID_S3-EX2-1.png?raw=true" width=700 />
<img src = "img/report/ID_S3-EX2-2.png?raw=true" width=700 />

## ID_S4
```
$> python loop_over_dataset_ID_S4.py
```

### ID_S4_EX1
<img src = "img/report/ID_S4-EX1-1.png?raw=true" width=800 />
<img src = "img/report/ID_S4-EX1-2.png?raw=true" width=800 />

### ID_S4_EX2
<img src = "img/report/ID_S4-EX2.png?raw=true" width=800 />

### ID_S4-EX3
#### (case 1) configs_det.use_labels_as_objects = False
* precision = 0.9620689655172414, recall = 0.9117647058823529
<img src = "img/report/ID_S4-EX3.png?raw=true" width=800 />

#### (case 2) configs_det.use_labels_as_objects = True
* precision = 1.0, recall = 1.0
<img src = "img/report/ID_S4-EX3-2.png?raw=true" width=800 />
