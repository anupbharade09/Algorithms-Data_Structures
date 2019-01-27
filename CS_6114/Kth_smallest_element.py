import sys
import os
import random
import operator

def kth_small(A,l,r,k):
    p = random.randint(0,6)

    A[r], A[k]= A[k], A[r]
    x= A[r]
    i= l
    for j in range(0,r-1):
        if A[j] <= x:
            A[i], A[j]= A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

    if i == k-1:
        return A[i]

    if i > k-1:
        return kth_small(A,l,i-1,k)

    return kth_small(A,i+1,r,k-i+L)

    return A[i]
