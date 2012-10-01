#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Title: linescan.py
## Description: simple routine to compute the intensity along a line on an image
## Author: Guillaume Gay <guillaume AT  mitotic-machine.org>

import numpy as np
import scipy.ndimage as ndi


def linescan(img, point1, point2, width = 1):

    '''
    Computes the interpolated intensity in a 2D image along a segment
    
    Parameters
    ----------
    img : 2d array
        The image.
    point1: x, y pair, float or int 
        x, y value of the segment origin
    point2: x, y pair, float or int 
        x, y value of the segment end
    width: int
        Width of the scan, perpendicular to the line

    Returns
    -------

    return_value : array
        The intensity profile along the line. The length of the profile
        is the ceil of the computed length of the line
    '''


    x1, y1 = point1 = np.asarray(point1, dtype = float)
    x2, y2 = point2 = np.asarray(point2, dtype = float)
    dx, dy = point2 - point1
    
    if x1 == x2:
        pixels = img[x1 - width / 2 :  x1 + width / 2 + 1,
                     min(y1, y2) : max(y1, y2)+1]
        intensities  = pixels.mean(axis = 0) 
        return intensities
    elif y1 == y2:

        pixels = img[min(x1, x2) : max(x1, x2)+1,
                     y1 - width / 2 :  y1 + width / 2 + 1]
        intensities = pixels.mean(axis = 1)
        return intensities

    theta = np.arctan2(dy,dx)
    a = dy/dx
    b = y1 - a * x1
    length = np.hypot(dx, dy)

    line_x = np.linspace(min(x1, x2), max(x1, x2), np.ceil(length))
    line_y = line_x * a + b 
    y_width = abs(width * np.sin(theta)/2)
    perp_ys = np.array([np.linspace(yi - y_width,
                                    yi + y_width, width) for yi in line_y])
    perp_xs = - a * perp_ys + (line_x +  a * line_y)[:, np.newaxis]

    perp_lines = np.array([perp_ys, perp_xs])
    pixels = ndi.map_coordinates(img, perp_lines)
    intensities = pixels.mean(axis = 1)

    return intensities


