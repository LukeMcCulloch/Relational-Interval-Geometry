#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:06:27 2019

@author: lukemcculloch
"""
import warnings
warnings.filterwarnings('ignore') #sorry, I've got old code that needs updating -- shame on me!


import numpy as np #linear algebra
#np.set_printoptions(precision=3)
#np.set_printoptions(threshold=3)

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

spline = rsp.curve #Bspline curve and surface module


automatic_differentiation = rsp.automatic_differentiation # just what it sounds like,
                                    # with vectors and intervals supported

adObjectMaker = automatic_differentiation.adObjectMaker

ad = automatic_differentiation.ad                   #automatic differentiation class

ia = rsp.ia                                         #interval analysis class



##
##*****************************************
## Make some AD (auto differentiation) numbers

num_in_vec = 2  # problem space size, in this toy example

identity = np.matrix(np.identity(num_in_vec))
nullmatrix = np.matrix(np.zeros((num_in_vec,num_in_vec),float))

# of_scalars=True     : means you intend to use this number in a vector of real numbers (False is default)
#x0 = ad( 2., N=num_in_vec, dim=0, of_scalars=True)
#x1 = ad( 2., N=num_in_vec, dim=1, of_scalars=True)

x0 = ad( 0.5, 
        grad = identity[0], 
        hess = nullmatrix, 
        of_scalars=True)
print 'x0.value = ',x0.value
print 'x0.grad  = ', x0.grad
print 'x0.hess  = '
print x0.hess

print type(x0.grad)


x1 = ad( 2., 
        grad = identity[1], 
        hess = nullmatrix, 
        of_scalars=True)

print ''
print 'x1.value = ',x1.value
print 'x1.grad  = ', x1.grad
print 'x1.hess  = '
print x1.hess

print type(x1.grad)


test = x0 + x1**2

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

dimensions = 2
order = 4

vertices=np.asarray([[0.,0.],
                     [2.,0.],
                     [3.0,0.],
                     [3.0,8.0],
                     [9.0,12.],
                     [11.,12.],
                     [12.,12.]])

num_in_vec = len(vertices)

xpts = []
ypts = []
for i in range(num_in_vec):
    xpti = vertices[i,0]
    ypti = vertices[i,1]
    xpts.append( ad( xpti, N=num_in_vec*dimensions, 
                    dim=i, of_scalars=True) )
    ypts.append( ad( ypti, N=num_in_vec*dimensions, 
                    dim=i+num_in_vec, of_scalars=True) )
    
curve1 = spline.Bspline(vertices,order)
curve1.plotcurve_detailed()
precompute_curve_integrals()



def fairness(curve, vertices=None):
    """
        Method to compute the non-weighted fairness 
        functionals of a B-spline curve.

    """        
    if vertices is None:
        xpts = curve.vertices[:,0]
        ypts = curve.vertices[:,1]
    else:
        xpts = vertices[0]
        ypts = vertices[1]
    E1 = np.dot(np.dot(xpts,curve.M1),xpts)+np.dot(np.dot(ypts,curve.M1),ypts)
    E2 = np.dot(np.dot(xpts,curve.M2),xpts)+np.dot(np.dot(ypts,curve.M2),ypts)
    E3 = np.dot(np.dot(xpts,curve.M3),xpts)+np.dot(np.dot(ypts,curve.M3),ypts)

    return E1,E2,E3

e1,e2,e3 = fairness(curve1, [xpts,ypts])

print curve1.E1
print curve1.E2
print curve1.E3

print e1
print e2
print e3

ADILS = rsp.ADILS
Lagrangian, IntervalLagrangeSpline = ADILS.Lagrangian, ADILS.IntervalLagrangeSpline
FormParameter = rsp.FormParameter  
FormParameterDict, generalized_aattractor = FormParameter.FormParameterDict, FormParameter.generalized_aattractor

initialValues  =  rsp.initialValues     
InitializeControlPoints, InitializeControlVertices, \
                                  interval_bounds, lagrangian_bounds = initialValues.InitializeControlPoints, initialValues.InitializeControlVertices, \
                                  initialValues.interval_bounds, initialValues.lagrangian_bounds
                                  


FPD = FormParameterDict(curve1) 
FPD.add_E1(kind='LS', weight = 1.)
FPD.add_E2(kind='LS', weight = .5)
FPD.add_E3(kind='LS', weight = .5)
FPD.add_ArcLengthApprox(kind='LS', weight = 1.)
FPD.add_AngleConstraint(kind='equality', location = 0., value = 0.)#AF.fuzzyNumber(-5.,-2.,0.))#
FPD.add_AngleConstraint(kind='equality', location = 1., value = 0.)
FPD.add_CurvatureConstraint(kind='equality', location = 0., value = 0.)
FPD.add_CurvatureConstraint(kind='equality', location = 1., value = 0.)


L = Lagrangian(FPD)
Lspline = IntervalLagrangeSpline(curve1, L)

vertices = Lspline.optimize()

Lspline.curve.plotcurve_detailed()