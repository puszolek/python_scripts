#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(N, M):
    
    A = [1] * N
    counter = 0
    
    for i in range (0, len(A)):
        if A[(i*M)%N] == 0:
            break
        else:
            A[(i*M)%N] = 0
            counter = counter + 1
    
    return counter
    
    pass