import random

class MaximumSum:

    def __init__(self,arr):
        self.__arr = arr
        self.length = len(arr)

    def maximumSumSubArr(self):
        curr_max = self.__arr[0]
        max_so_far = self.__arr[0]
        for i in range(1, self.length):
            curr_max = max(self.__arr[i], curr_max + self.__arr[i])
            max_so_far = max(curr_max, max_so_far)
        return max_so_far

    def maximumSumExactlyKEle(self,K):
        curr_max = 0

        for i in range(K):
            curr_max += self.__arr[i]

        max_so_far = curr_max

        for i in range(K, self.length):
            curr_max += self.__arr[i]
            curr_max -= self.__arr[i - K]
            max_so_far = max(curr_max, max_so_far)

        return max_so_far

    def maximumSumAMKEle(self,K):
        curr_max = self.__arr[0]
        max_so_far = self.__arr[0]
        tempK = 0
        for i in range(1,self.length):
            if self.__arr[i] >= curr_max + self.__arr[i]:
                curr_max = self.__arr[i]
                tempK = 0
            else:
                curr_max = curr_max + self.__arr[i]
                tempK += 1
            if tempK >= K:
                curr_max = curr_max - self.__arr[i - K]

            max_so_far = max(curr_max, max_so_far)

        return max_so_far

    def maximumSumALKEle(self,K):
        curr_max = self.__arr[0]
        maxSum = list()
        maxSum.append(self.__arr[0])
        for i in range(1, self.length):
            curr_max = max(curr_max + self.__arr[i], self.__arr[i])
            maxSum.append(curr_max)

        sum = 0
        for i in range(K):
            sum = sum + self.__arr[i]

        max_so_far = sum
        for i in range(K, self.length):
            sum += self.__arr[i] - self.__arr[i - K]
            max_so_far = max(max_so_far, sum, sum + maxSum[i - K])

        return max_so_far


#arr = [-100,100,100,-100,-500,-500,-1,50,50,-1]
arrLen = int(input())
arr = [random.randint(-100,100) for i in range(arrLen)]
print(arr)
m1 = MaximumSum(arr)
K = 4
print(m1.maximumSumSubArr())
print(m1.maximumSumALKEle(K))
print(m1.maximumSumAMKEle(K))
print(m1.maximumSumExactlyKEle(K))