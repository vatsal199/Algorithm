'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''
# https://practice.geeksforgeeks.org/problems/inversion-of-array/0/
# Find inversion
# Here we use merge sort algorithm to find inversion
# Below solution is exact merge sort except line no 15 added
def merge(arr,low,high):
    count = 0
    mid = int((low+high)/2)
    p = low
    q = mid+1
    temp = []
    while p <= mid and q <= high:
        if arr[p] > arr[q]:
            # whenever we add element from right sub array in temp array at that time
            # we have to add no of element remain(including current) in left sub array in count
            count += mid-p+1
            temp.append(arr[q])
            q += 1
        else:
            temp.append(arr[p])
            p += 1

    while q <= high:
        temp.append(arr[q])
        q += 1

    while p <= mid:
        temp.append(arr[p])
        p += 1

    for i in temp:
        arr[low] = i
        low += 1

    return count



def partition(arr,low,high):
    count = 0
    if low < high:
        mid = int((low+high)/2)

        count += partition(arr,low,mid)
        count += partition(arr,mid+1,high)
        count += merge(arr,low,high)

    return count

Tc = int(input())
while Tc != 0:
    arrLen = int(input())
    inp = input().split()
    arr = [int(i) for i in inp]
    count = partition(arr,0,arrLen-1)
    print(count)
    Tc -= 1