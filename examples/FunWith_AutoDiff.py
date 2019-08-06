#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:06:27 2019

@author: lukemcculloch
"""

import numpy as np #linear algebra

# import my feasible form parameter design PhD code-dump/library
import relational_lsplines as rsp


def precompute_curve_integrals():

    curve1.basis_matrix()
    curve1.pts_M_pts() #arc length precomputation
    curve1.compute_arclength()
    curve1.MomentMatrices()
    curve1.fairness()
    curve1.compute_area()
    return

curve = rsp.curve #Bspline curve and surface module


automatic_differentiation = rsp.automatic_differentiation # just what it sounds like,
                                    # with vectors and intervals supported

adObjectMaker = automatic_differentiation.adObjectMaker

ad = automatic_differentiation.ad #

ia = rsp.ia #interval analysis


num_in_vec = 2


##
##*****************************************
## Make some AD (auto differentiation) numbers

# of_scalars=True     : means you intend to use this number in a vector of real numbers (False is default)
x0 = ad( 2., name = 'x', 
        N=num_in_vec, dim=0, of_scalars=True)
y1 = ad( 2., name = 'x', 
        N=num_in_vec, dim=1, of_scalars=True)

test = xf + yf**2

print '\ntest value'
print test.value
print '\ntest gradient'
print test.grad
print '\ntest hessian'
print test.hess



##
##*****************************************
##  how about a B-spline?
##
##
## do things by hand to show that it works..

order = 4
num_in_vec = 7

vertices=np.asarray([[0.,0.],
                     [2.,0.],
                     [3.0,0.],
                     [6.0,5.],
                     [9.0,12.],
                     [11.,12.],
                     [12.,12.]])

xpts = []
ypts = []
for i in range(num_in_vec):
    xpti = vertices[i,0]
    ypti = vertices[i,0]
    xpts.append( ad( xpti, name = 'x'+str(i), 
        N=num_in_vec, dim=0, of_scalars=True) )
    ypts.append( ad( xpti, name = 'x'+str(i), 
        N=num_in_vec, dim=0, of_scalars=True) )
    
curve1 = curve.Bspline(vertices,order)
curve1.plotcurve_detailed()
precompute_curve_integrals()