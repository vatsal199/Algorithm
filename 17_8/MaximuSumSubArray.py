TC = int(input())
while TC != 0:
    arrLen = int(input())
    inp = input().split()
    arr = [int(i) for i in inp]
    curr_max = arr[0]
    max_so_far = arr[0]
    for i in range(1,arrLen):
        curr_max = max(arr[i],curr_max+arr[i])
        max_so_far = max(curr_max,max_so_far)
    print(max_so_far)
    TC -= 1