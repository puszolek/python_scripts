#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A, K):
    # write your code in Python 2.7
    
    if len(A) == 1 or len(A) == 0:
        return A
    
    n = len(A)
    a = []
    while K >=1:
        a = A[:]
        a[0] = A[-1]
        a[1:] = A[:-1]
        A = a[:]
        K = K - 1
            
    return a
    
    pass