# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:06:40 2020

@author: User
"""


def knapSackNoRep(capacity, bars):
    amount = len(bars)
    value=[[0 for row in range(0, amount+1)] for col in range(0, capacity+1)]
    for i in range(1, amount+1):
        wi = bars[i-1]
        vi = bars[i-1]
        for w in range(1, capacity+1):
            value[w][i] = value[w][i-1]
            if wi <= w:
                val = value[w-wi][i-1] + vi
                if value[w][i] < val:
                    value[w][i] = val
    return value[capacity][amount]




if __name__ == '__main__':
   
    
    
    W, n     = [int(i) for i in input().split()]
    w       = [int(i) for i in input().split()]
    print(knapSackNoRep(W, w))