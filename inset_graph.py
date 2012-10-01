#!/usr/bin/env python

# test script to insert custom subplots within subplots
# jr -- 20090223



import matplotlib
from matplotlib import pyplot as plt


def inset_graph():



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
 
