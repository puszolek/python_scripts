#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A):
    
    a = sorted(A)
    
    x = a[0]*a[1]*a[2]
    y = a[0]*a[1]*a[-1]
    z = a[0]*a[-2]*a[-1]
    q = a[-3]*a[-2]*a[-1]
    
    b = [x, y, z, q]
    
    return max(b)
    
    pass