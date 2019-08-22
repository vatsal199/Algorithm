import random
import time

class HeapSort:
    __arr = list()
    heapSize = 0
    length = 0

    def __init__(self,arr):
        self.__arr = arr
        self.heapSize = len(arr)
        self.length = self.heapSize

    def sort(self):
        self.buildMaxHeap()
        while self.heapSize > 0:
            self.deleteMax()

    def deleteMax(self):
        arr[self.heapSize - 1], arr[0] = arr[0], arr[self.heapSize - 1]
        self.heapSize -= 1
        self.topDownHeapify(0)

    def printArr(self):
        for ele in self.__arr:
            print(ele,end=" ")
        print()

    def buildMaxHeap(self):
        for i in range(int(self.heapSize/2),-1,-1):
            self.topDownHeapify(i)

    def add(self,x):
        self.__arr.append(x)
        self.heapSize += 1
        self.bottomUpHeapify(self.heapSize-1)

    def bottomUpHeapify(self,i):
        parent = int((i-1)/2)
        while parent >= 0:
            if self.__arr[parent] < self.__arr[i]:
                self.__arr[parent],self.__arr[i]  = self.__arr[i],self.__arr[parent]
                i = parent
                parent = int((i-1)/2)
            else:
                break

    def topDownHeapify(self,i):
        left = 2*i + 1
        right = 2*i + 2

        while right < self.heapSize:
            if self.__arr[left] > self.__arr[i]:
                largest = left
            else:
                largest = i

            if self.__arr[right] > self.__arr[largest]:
                largest = right

            if largest != i:
                self.__arr[i],self.__arr[largest] = self.__arr[largest],self.__arr[i]
                i = largest
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break

        if left<self.heapSize and self.__arr[left] > self.__arr[i]:
            self.__arr[i],self.__arr[left] = self.__arr[left],self.__arr[i]


inp = int(input())
arr = [random.randint(0,100) for i in range(inp)]
h1 = HeapSort(arr)
#h1.printArr()
now = time.time()*1000
h1.sort()
then = time.time()*1000
milliSec = int(round(then-now))
print(milliSec)
#h1.printArr()
