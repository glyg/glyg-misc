#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Title: 
## Description: 
## Author:uillaume Gay<elagachado AT  gmail DOT com>
## Commentary:
from opencv import cv

def mean_box(b1, b2):
    '''
    return the "mean" box from two CvBox2D
    '''

    bm = cv.CvBox2D()
    bm.center.x = (b1.center.x + b2.center.x)/2.
    bm.center.y = (b1.center.y + b2.center.y)/2.
    bm.angle = (b1.angle + b2.angle)/2. 
    bm.size.width = (b1.size.width + b2.size.width)/2.
    bm.size.height = (b1.size.height + b2.size.height)/2.

    return bm
