#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Title: 
## Description: 
## Author:uillaume Gay<elagachado AT  gmail DOT com>
## Commentary:

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
