#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    n = int(len(q))
    swap = 0
    for i in range(n):
        for j in range(i):      #for elements before q[i]
            if(q[i]<q[j]):      #comparing ith and all (i-1)'s elements
                swap+=1
            
        if(q[i]-(i+1) > 2):
            print("Too chaotic")
            return
    print (swap)

            
      

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
