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


num_in_vec = 2


##
##*****************************************
## Make some AD (auto differentiation) numbers

# of_scalars=True     : means you intend to use this number in a vector of real numbers (False is default)
xf = ad( 2., name = 'x', 
        N=num_in_vec, dim=0, of_scalars=True)
yf = ad( 2., name = 'x', 
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
## 