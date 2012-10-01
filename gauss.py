#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Title: 
## Description: 
## Author:uillaume Gay<elagachado AT  gmail DOT com>
## Commentary:

#from numpy import *
import numpy as np


def gauss1(z, z0 = 0., A = 1., sigma = 1.):
    '''

    '''
    return A * np.exp(-2*((z - z0)/(sigma))**2)


def gauss2( xs , ys, x0 = 0., y0 = 0., Ax = 1/sqrt(2*pi),
            Ay = 1/sqrt(2*pi), sigmax = 1., sigmay = 1.):

    xs = asarray(xs)
    ys = asarray(ys)
    if xs.size == 1 and ys.size == 1:
        return Ax * Ay * ( gauss1(xs, x0, A = 1, sigma = sigmax)
                           * gauss1(ys, y0, A = 1, sigma = sigmay))
    h = zeros((xs.shape[0], ys.shape[0]), dtype = 'float')
    idxs = ndindex(xs.shape[0], ys.shape[0])
    for i in idxs:
        h[i] = Ax * Ay * ( gauss1(xs[i[0]], x0, A = 1, sigma = sigmax)
                           * gauss1(ys[i[1]], y0, A = 1, sigma = sigmay))
    return h
