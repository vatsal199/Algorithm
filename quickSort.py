'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''
import time
import random

def pivot(arr,low,high):
    p = low+1
    q = high
    while p<=q:
        while q>low and arr[q]>=arr[low]:
            q -= 1
        while p<=high and arr[p] < arr[low]:
            p += 1

        if p<q:
            arr[p],arr[q] = arr[q],arr[p]

    arr[low],arr[q] = arr[q],arr[low]
    return q

def partation(arr,low,high):
    if low<high:
        i = pivot(arr,low,high)
        partation(arr,low,i-1)
        partation(arr,i+1,high)

arrLen = int(input())
arr = [random.randint(1,1000) for i in range(arrLen)]
#arr = [(arrLen - i) for i in range(arrLen)]
#print(arr)
now = time.time()*1000
partation(arr,0,arrLen-1)
then = time.time()*1000
milliSec = int(round(then-now))
print(milliSec)



