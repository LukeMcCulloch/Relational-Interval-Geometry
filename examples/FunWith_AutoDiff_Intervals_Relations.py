#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:06:27 2019

@author: lukemcculloch
"""

# import my feasible form parameter design PhD code-dump/library
import relational_lsplines as rsp



curve = rsp.curve #Bspline curve and surface module


automatic_differentiation = rsp.automatic_differentiation # just what it sounds like,
                                    # with vectors and intervals supported

adObjectMaker = automatic_differentiation.adObjectMaker

ad = automatic_differentiation.ad #

ia = rsp.ia #interval analysis


N=2

# of_scalars=True     : means you intend to use this number in a vector of real numbers (False is default)
xf = ad( 2., name = 'x', N=2, dim=0, of_scalars=True)




#
#*****************************************
# switch to intervals 
x0grad = adObjectMaker.makeGradient(N,i=0)
x0hess = adObjectMaker.makeHessian(N)

# of_scalars=False    : means you intend to use this ad number in a vector of interval numbers (False is default)
xi = ad( 2., 
        grad = x0grad, 
        hess = x0hess,
        name = 'x', N=2, dim=0,
        of_scalars=False )