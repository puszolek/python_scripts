#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def solution(N):
    binary = ''
    
    while N >= 1:
        if N%2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        N = math.floor(N/2)

    count = 0
    list = []

    for i in range (0, len(binary)):
        if binary[i] == '0':
            count = count+1
        else:
            list.append(count)
            count = 0

    return max(list)
	
print solution(13)