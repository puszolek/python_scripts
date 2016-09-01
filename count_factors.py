#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(N):

    if N%2 != 0:
        n = (N-1)/2
    else:
        n = N/2
    A = [i for i in range(2, n+1)]
    A.append(N)

    factors = []
    for i in A:
        if N%i == 0:
            factors.append(i)
            factors.append(N/i)

    return len(set(factors))

    pass