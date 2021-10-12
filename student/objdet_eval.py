# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Evaluate performance of object detection
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# general package imports
import numpy as np
import matplotlib
matplotlib.use('wxagg') # change backend so that figure maximizing works on Mac as well     
import matplotlib.pyplot as plt

import torch
from shapely.geometry import Polygon
from operator import itemgetter

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# object detection tools and helper functions
import misc.objdet_tools as tools

def calculate_iou(gt_bbox, pred_bbox):
    x11,y11,x12,y12 = gt_bbox
    x21,y21,x22,y22 = pred_bbox
    print('x11 = {}, y11 = {}, x12 = {}, y12 = {}'.format(x11,y11,x12,y12))
    print('x21 = {}, y21 = {}, x22 = {}, y22 = {}'.format(x21,y21,x22,y22))

    area_of_box1 = abs((x12-x11)*(y12-y11))
    area_of_box2 = abs((x22-x21)*(y22-y21))

    x_diff,y_diff = 0,0
    if x11 <= x21 <= x12 or x11 <= x22 <= x12 or x21 <= x11 <= x22 or x21 <= x12 <= x22:
        x_diff = min(x12,x22)-max(x11,x21)

    if y11 <= y21 <= y12 or y11 <= y22 <= y12 or y21 <= y11 <= y22 or y21 <= y12 <= y22:
        y_diff = min(y12,y22)-max(y11,y21)

    intersect = x_diff * y_diff
    print('x_diff = {}'.format(x_diff))
    print('y_diff = {}'.format(y_diff))
    print('intersect = {}'.format(intersect))
    print('area_of_box1 = {}'.format(area_of_box1))
    print('area_of_box2 = {}'.format(area_of_box2))
    iou = intersect / (area_of_box1 + area_of_box2 - intersect)
    print('iou = ', iou)
    return iou


# compute various performance measures to assess object detection
def measure_detection_performance(detections, labels, labels_valid, min_iou=0.5):

     # find best detection for each valid label 
    true_positives = 0 # no. of correctly detected objects
    center_devs = []
    ious = []
    for label, valid in zip(labels, labels_valid):
        matches_lab_det = []
        if valid: # exclude all labels from statistics which are not considered valid
            
            # compute intersection over union (iou) and distance between centers

            ####### ID_S4_EX1 START #######     
            #######
            print("student task ID_S4_EX1 ")

            ## step 1 : extract the four corners of the current label bounding-box
            gt_fl = (label.box.center_x - 0.5 * label.box.length, label.box.center_y - 0.5 * label.box.width)
            # gt_rl = (label.box.center_x - 0.5 * label.box.length, label.box.center_y + 0.5 * label.box.width)
            gt_rr = (label.box.center_x + 0.5 * label.box.length, label.box.center_y + 0.5 * label.box.width)
            # gt_rf = (label.box.center_x + 0.5 * label.box.length, label.box.center_y - 0.5 * label.box.width)

            gt_bbox = (max(0,gt_fl[0]), max(0,gt_fl[1]), max(0,gt_rr[0]), max(0,gt_rr[1]))
            gt_center = (label.box.center_x, label.box.center_y)

            ## step 2 : loop over all detected objects
            for det in detections:

                ## step 3 : extract the four corners of the current detection
                _, x, y, _, _, w, l, yaw = det
                fl, rl, rr, rf = tools.compute_box_corners(x,y,w,l,yaw)

                min_x = max(0,min(fl[0], rl[0], rr[0], rf[0]))
                min_y = max(0,min(fl[1], rl[1], rr[1], rf[1]))
                max_x = max(0,max(fl[0], rl[0], rr[0], rf[0]))
                max_y = max(0,max(fl[1], rl[1], rr[1], rf[1]))

                pred_bbox = (min_x, min_y, max_x, max_y)
                pred_center = (fl[0] + 0.5*(rr[0]-fl[0]), fl[1] + 0.5*(rr[1]-fl[1]))
                ## step 4 : computer the center distance between label and detection bounding-box in x, y, and z
                dist_x = abs(gt_center[0] - pred_center[0])
                dist_y = abs(gt_center[1] - pred_center[1])
                dist_z = 0
                ## step 5 : compute the intersection over union (IOU) between label and detection bounding-box
                iou = calculate_iou(gt_bbox, pred_bbox)

                ## step 6 : if IOU exceeds min_iou threshold, store [iou,dist_x, dist_y, dist_z] in matches_lab_det and increase the TP count
                if iou > min_iou:
                    matches_lab_det.append([iou, dist_x, dist_y, dist_z])
                    true_positives += 1
            #######
            ####### ID_S4_EX1 END #######     
            
        # find best match and compute metrics
        if matches_lab_det:
            best_match = max(matches_lab_det,key=itemgetter(1)) # retrieve entry with max iou in case of multiple candidates   
            ious.append(best_match[0])
            center_devs.append(best_match[1:])


    ####### ID_S4_EX2 START #######     
    #######
    print("student task ID_S4_EX2")
    
    # compute positives and negatives for precision/recall
    
    ## step 1 : compute the total number of positives present in the scene
    all_positives = len(detections)

    ## step 2 : compute the number of false negatives (true negative??)
    false_negatives = len(labels) - true_positives

    ## step 3 : compute the number of false positives
    false_positives = all_positives - true_positives
    
    #######
    ####### ID_S4_EX2 END #######     
    
    pos_negs = [all_positives, true_positives, false_negatives, false_positives]
    det_performance = [ious, center_devs, pos_negs]
    
    return det_performance


# evaluate object detection performance based on all frames
def compute_performance_stats(det_performance_all):

    # extract elements
    ious = []
    center_devs = []
    pos_negs = []
    for item in det_performance_all:
        ious.append(item[0])
        center_devs.append(item[1])
        pos_negs.append(item[2])
    
    ####### ID_S4_EX3 START #######     
    #######    
    print('student task ID_S4_EX3')

    # pos_negs = [all_positives, true_positives, false_negatives, false_positives]
    # det_performance = [ious, center_devs, pos_negs]

    ## step 1 : extract the total number of positives, true positives, false negatives and false positives
    total_all_positive = 0
    total_true_positive = 0
    total_false_negative = 0
    total_false_positive = 0

    for pos_neg in pos_negs:
        all_positive, true_positive, false_negative, false_positive = pos_neg
        total_all_positive += all_positive
        total_true_positive += true_positive
        total_false_negative += false_negative
        total_false_positive += false_positive

    ## step 2 : compute precision
    precision = total_true_positive / total_all_positive

    ## step 3 : compute recall 
    recall = total_true_positive / total_true_positive + total_false_negative

    #######    
    ####### ID_S4_EX3 END #######     
    print('precision = ' + str(precision) + ", recall = " + str(recall))   

    # serialize intersection-over-union and deviations in x,y,z
    ious_all = [element for tupl in ious for element in tupl]
    devs_x_all = []
    devs_y_all = []
    devs_z_all = []
    for tuple in center_devs:
        for elem in tuple:
            dev_x, dev_y, dev_z = elem
            devs_x_all.append(dev_x)
            devs_y_all.append(dev_y)
            devs_z_all.append(dev_z)
    

    # compute statistics
    stdev__ious = np.std(ious_all)
    mean__ious = np.mean(ious_all)

    stdev__devx = np.std(devs_x_all)
    mean__devx = np.mean(devs_x_all)

    stdev__devy = np.std(devs_y_all)
    mean__devy = np.mean(devs_y_all)

    stdev__devz = np.std(devs_z_all)
    mean__devz = np.mean(devs_z_all)
    #std_dev_x = np.std(devs_x)

    # plot results
    data = [precision, recall, ious_all, devs_x_all, devs_y_all, devs_z_all]
    titles = ['detection precision', 'detection recall', 'intersection over union', 'position errors in X', 'position errors in Y', 'position error in Z']
    textboxes = ['', '', '',
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_x_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_x_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), ))),
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_y_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_y_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), ))),
                 '\n'.join((r'$\mathrm{mean}=%.4f$' % (np.mean(devs_z_all), ), r'$\mathrm{sigma}=%.4f$' % (np.std(devs_z_all), ), r'$\mathrm{n}=%.0f$' % (len(devs_x_all), )))]

    f, a = plt.subplots(2, 3)
    a = a.ravel()
    num_bins = 20
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    for idx, ax in enumerate(a):
        ax.hist(data[idx], num_bins)
        ax.set_title(titles[idx])
        if textboxes[idx]:
            ax.text(0.05, 0.95, textboxes[idx], transform=ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
    plt.tight_layout()
    plt.show()

