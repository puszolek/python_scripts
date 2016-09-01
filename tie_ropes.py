#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(K, A):
    
    a = sorted(A)
    
    if sum(a) < K:
        return 0
    if sum(a) == K:
        return 1
    
    length = 0
    counter = 0
    for i in A:
        length = length + i
        if length >= K:
            counter = counter + 1
            length  = 0
    return counter

    pass