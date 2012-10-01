#!/usr/bin/python
# -*- coding: utf-8 -*-

# Miscelaneous utilities
# Guillaume 07/27/08


from scipy import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt











def inset_graph():

    #!/usr/bin/env python

    # test script to insert custom subplots within subplots
    # jr -- 20090223


    fig = plt.figure(figsize=(8,6))
    fw = fig.get_figwidth()*fig.get_dpi()
    fh = fig.get_figheight()*fig.get_dpi()

    x = np.linspace(1,10,100)
    y = np.sin(x)

    for i in range(4):
        ax = fig.add_subplot(2,2,i+1)
        ax.plot(x,3+y,'b-')
        ax.set_ylim(0,4.5)

        Bbox = matplotlib.transforms.Bbox.from_bounds(.4, .1, .5, .3)
        trans = ax.transAxes + fig.transFigure.inverted()
        l, b, w, h = matplotlib.transforms.TransformedBbox(Bbox, trans).bounds
        axins = fig.add_axes([l, b, w, h])

        axins.plot(x,y,'r-')

    fig.show() 

def mean_sqr_disp(traj):
     
    traj = np.asarray(traj)
    if len(traj.shape) > 1:
        print 'higher dimensions not yet supported'
        return 0

    T = traj.size
    msd = np.zeros(T-1)

    for n in range(T - 1):
        sqrd = (traj[:T-n] - traj[n:T])**2
        msd[n]  = sum(sqrd[isfinite(sqrd)]) / sqrd[isfinite(sqrd)].size

    return msd


def first_min(wave):
    '''
    returns the first minimum of an array, starting from the first element 
    if interp = True, evaluates the minimum position via linear interpolation
    of diff(wave)

    '''
    
    for i in range(1,wave[1:-1].size):
        if wave[i-1] > wave[i] < wave[i+1]:
            return i
    return None
        
def fwhm(wave):
    '''
    Returns full width at half maximum
    '''
    
    m = wave.max()
    x = wave.argmax()

    right = left = nan
    
    wave /= m
    for i in range(min(wave[x:-1].size, wave[1:x].size)):
        if wave[x+i] <= 0.5 < wave[x+i+1]:
            right = i
        if wave[x-i] <= 0.5 < wave[x-i-1]:
            left = i

        if isfinite(right) and isfinite(left):
            return right + left

#def gauss2(z, z0 = 0, A = 1/sqrt(2*pi), sigma = 1)
    
