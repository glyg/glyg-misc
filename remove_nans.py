#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Title: 
## Description: 
## Author:uillaume Gay<elagachado AT  gmail DOT com>
## Commentary:

from numpy import array, isfinte, column_stack

def remove_nans(array_tuple):
    
    omat = column_stack(array_tuple)
    nmat = []
    for n in range(omat.shape[0]):
        if all(isfinite(omat[n,:])):
            nmat.append(omat[n,:])

    nmat = array(nmat)
    

    news = []
    for m in range(nmat.shape[1]):
        news.append(nmat[:,m])

    return tuple(news)
