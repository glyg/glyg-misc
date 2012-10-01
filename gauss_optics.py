#!/usr/bin/python
# -*- coding: utf-8 -*-

# Gaussian optics utils...
# Guillaume 07/27/08


from scipy import *
from my_utils import *

C = 299792458



# E(r,z) = E_0 \frac{w_0}{w(z)} \exp \left(
# \frac{-r^2}{w^2(z)}\right) \exp \left( -ikz -ik \frac{r^2}{2R(z)}
#     +i \zeta(z) \right)\ ,


class CircularGaussBeam(object):

    def __init__(self, wavelength, w0, E0):
        '''
        wavelength in meters
        w0: waist at focal point in meters
        E0 : electric field amplitude
        n : refractive index of the environement
        '''

        self.wavelength = wavelength
        self.w0 = w0
        self.E0 = E0

        self.zR = pi * w0**2 / wavelength # Rayleigh range
        self.div = self.wavelength / (pi * w0)
        self.k0 = 2 * pi / wavelength #vaccum wave number (m^-1)
        self.omega = self.k0 / C #pulsation
        self.frequency = self.omega / (2 * pi )

        
    def waist(self, z):
        '''
        returns fields waist at distance z of the focal point
        '''
        return self.w0 * sqrt(1 + (z/self.zR)**2)
        
    def gouy(self, z):
        '''
        returns the Gouy phase at distance z
        '''
        return arctan2( z , self.zR)
        
    def curv(self, z):
        '''
        returns the radius of curvature of the wavefront at distance z
        '''
        if z == 0:
            return inf
        else:
            return z * (1 + (self.zR/z)**2)
        

    def efield(self, r , z):
        '''
        returns the electric field amplitude and phase at point r,z
        '''

        norme = self.E0 * (self.w0/self.waist(z)) * exp(- (r / self.waist(z))**2) 

        i = (0.0+1.0j)
        k = self.k0
        
        R = vectorize(self.curv)(z)
        phase = i * ( - k * z - k * r**2 / (2 * R) + self.gouy(z))

        return norme * exp(phase)

    def intensity(self, r, z):

        w = self.waist(z)
        return abs(self.E0**2) * (self.w0/w)**2 * exp( -2* (r/w)**2)


class EllipticGaussBeam(CircularGaussBeam):

    def __init__(self, wavelength, wx, wy, E0):

        self.gx = CircularGaussBeam(wavelength, wx, 1)
        self.gy = CircularGaussBeam(wavelength, wy, 1)        
        self.wavelength = wavelength

        self.E0 = E0
        self.wx = wx
        self.wy = wy
        self.zRx = pi * wx**2 / wavelength # Rayleigh range
        self.zRy = pi * wy**2 / wavelength # Rayleigh range
        
        self.divx = self.wavelength / (pi * wx)
        self.divx = self.wavelength / (pi * wy)
        
        self.k0 = 2 * pi / wavelength #vaccum wave number (m^-1)
        self.omega = self.k0 / C #pulsation
        self.frequency = self.omega / (2 * pi )

    
    def efield(self, x,y,z):

        
        norme = self.E0 * ( sqrt(self.wx*self.wy/(self.gx.waist(z)*self.gy.waist(z)))
                         * exp(- (x / self.gx.waist(z))**2 -  (x / self.gx.waist(z))**2))
        
        i = (0.0+1.0j)
        k = self.k0
        
        Rx = vectorize(self.gx.curv)(z)
        Ry = vectorize(self.gy.curv)(z)
        
        phase = i * ( - k * z - k * x**2 / (2 * Rx)- k * y**2 / (2 * Ry)
                      + self.gx.gouy(z)/2 + self.gy.gouy(z)/2 )

        return norme * exp(phase)


    def intensity(self, x, y, z):

        wxz = self.gx.waist(z)
        wyz = self.gy.waist(z)
        
        I = (abs(self.E0**2) * ( self.wx*self.wy/(wxz*wyz)) *
                                exp( -2* ((x/wxz)**2 + (y/wyz)**2)))

        return I
