#!/usr/bin/python
# -*- coding: utf-8 -*-

##Définitions  pour les simulations de la cellule ###

import scipy as S
from math import *


class Position(object):
    ### position dans un espace  dimensions 
    def __init__(self, pos=S.zeros(3)):
        self.pos = pos
    
    def move(self, da, db, dc):
        
        self.pos[0] += da
        self.pos[1] += db
        self.pos[2] += dc

 
class CartezPos(Position):
    ### En coordonéees cartésiennes, 2D ou 3D

    def norme(self):
        pos = self.pos
        x = pos[0]
        y = pos[1]
        if len(pos) == 3:
            z = pos[2]
        else:
            z = 0
        
        rho = sqrt(x**2+y**2+z**2)
        return rho

    def spherical(self):
        ''' returns a 3D array in the spherical coordiantes system '''
        pos = self.pos
        x = pos[0]
        y = pos[1]
        z = pos[2]
        rho = self.norme()
        theta = atan2(y, x)
        if rho == 0:
            phi = 0
        else:
            phi = acos(z/rho)

        spherpos = S.array([rho,theta,phi])
        return spherpos

    def distance(self,other):
        ''' Calulates the distance between two position
        pos1 and pos2 must be 2D or 3D arrays
        '''
        pos1 = self.pos
        pos2 = other.pos
        p12 = CartezPos(pos2 - pos1)
        dist = p12.norme()
        return dist
        
class SpherPos(Position):
    # On note (rho, theta, phi), i.e. : (norme, azimuth, zenith)
    def norme(self):
        pos = self.pos
        rho = pos[0]

        return rho

    def cartez(self):
        ''' outputs a 3D array in the cartesian coordinates system '''
        pos = self.pos
        rho = pos[0]
        theta = pos[1]
        phi = pos[2]

        x = rho * cos(theta) * sin(phi)
        y = rho * sin(theta) * sin(phi)
        z = rho * cos(phi)

        cpos = S.array([x, y, z])
        return cpos
        
    def distance(self,other):

        pos1 = self.pos
        pos2 = other.pos

        cpos1 = CartezPos(self.cartez())
        cpos2 = CartezPos(other.cartez())
        
        dist = cpos1.distance(cpos2)
        return dist
        
        
                  
class Trajectoire(Position):
    ### c'est un liste de positions
    def __init__(self):
        self.traj = []

def distance(pos1,pos2):
    ''' Outputs the distance between 2 points in the cartesian coords
    (whether 2 or 3 dimensions)
    '''
    pos1 = CartezPos(pos1)
    pos2 = CartezPos(pos2)
    return pos1.distance(pos2)
        
