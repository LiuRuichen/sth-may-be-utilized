# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:57:20 2021
"""
'''
有关矩阵的特征值分解的问题
如果A是实对称矩阵，则必存在A = VDV.T,这里V是正交矩阵，即列向量彼此正交,且向量的模长都是1,满足V.T = inv(V)
在numpy的eig函数中,有时候分解是按照A = V*D*inv(V),所以我们有时候需要进行施密特正交化处理,使得A = VDV.T
'''

import numpy as np
from sympy.matrices import Matrix, GramSchmidt
from numpy.linalg import eig

A = np.array([[4, 2, 2],
       [2, 4, 2],
       [2, 2, 4]])


vals, vecs = eig(A)

print(vecs, vals)

print('A:', np.dot(np.dot(vecs, np.diag(vals)), np.linalg.inv(vecs))) #A = vecs * Diag * vecs^(-1),没有经过施密特正交化

L = [Matrix(vecs[:,0].tolist()), Matrix(vecs[:,2].tolist())]
o1 = GramSchmidt(L, True) #施密特正交化
arr = np.array(o1)
print(arr)
vecs[:,0] = arr[1].reshape((3,))
vecs[:,2] = arr[0].reshape((3,))

print(vecs)
'''
[[ 0.          0.57735027 -0.81649658]
 [-0.70710678  0.57735027  0.40824829]
 [ 0.70710678  0.57735027  0.40824829]]
 '''

print(np.dot(np.dot(vecs, np.diag(vals)), vecs.T)) #检验A = vecs * diag(vals) * vecs.T
'''
[[4. 2. 2.]
 [2. 4. 2.]
 [2. 2. 4.]]
 '''
 
#检验是否为特征向量
print(np.dot(A,vecs[:,2])) 
print(np.dot(vals[2],vecs[:,2]))
'''
[-1.63299316  0.81649658  0.81649658]
[-1.63299316  0.81649658  0.81649658]
相等，所以AX = lambda*X
'''

#检验向量是否为正交向量
print(np.dot(vecs[:,0], vecs[:,1]))
print(np.dot(vecs[:,2], vecs[:,1]))
print(np.dot(vecs[:,0], vecs[:,2]))
'''
-5.551115123125783e-17
-8.326672684688674e-17
-5.551115123125783e-17
'''

#检验是否为单位向量
print(np.sqrt(np.dot(vecs[:,0],vecs[:,0]))) #0.9999999999999999
print(np.sqrt(np.dot(vecs[:,1],vecs[:,1]))) #1.0
print(np.sqrt(np.dot(vecs[:,2],vecs[:,2]))) #1.0