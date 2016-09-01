#!/usr/bin/env python
# -*- coding: utf-8 -*-


ef solution(S):
    
    if len(S) == 0:
        return 1
        
    begining = ['[', '{', '(']
    diction = {
        ']' : '[', 
        '}' : '{', 
        ')' : '(',
        }
    
    a = []
    for i in S:
        if i in begining:
            a.append(i)
        else:
            if len(a) == 0:
                return 0
            elif diction[i] != a.pop():
                return 0
                
    if len(a) == 0:
        return 1
    else:
        return 0
        
    pass