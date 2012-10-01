#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy, Image

def image2array(im):
     """Convert image to numpy array"""
     if im.mode not in ("I;16"):
          a = numpy.asarray(im)
     if im.mode == "I;16":
         a = numpy.fromstring(im.tostring(), numpy.uint16)
     a.shape = im.size[1], im.size[0]
     return a

def array2image(a):
     """Convert numpy array to image"""
     if a.dtype.type == numpy.uint16:
          mode = "I;16"
          return Image.fromstring(mode, (a.shape[1], a.shape[0]), a.tostring())
     else:
          
          return Image.fromarray(a)

