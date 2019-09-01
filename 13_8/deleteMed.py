'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''
import random
import time

class MinHeap:
    __arr = list()
    heapSize = 0
    length = 0

    def __init__(self,arr):
        self.__arr = arr
        self.heapSize = len(arr)
        self.length = self.heapSize

    def getMin(self):
        return self.__arr[0]

    def deleteMin(self):
        temp = self.__arr[0]
        self.__arr[self.heapSize - 1], self.__arr[0] = self.__arr[0], self.__arr[self.heapSize - 1]
        self.heapSize -= 1
        self.topDownHeapify(0)
        return temp

    def printArr(self):
        for ele in self.__arr:
            print(ele,end=" ")
        print()

    def printHeap(self):
        for i in range(self.heapSize):
            print(self.__arr[i],end=" ")
        print()

    def buildMaxHeap(self):
        for i in range(int(self.heapSize/2),-1,-1):
            self.topDownHeapify(i)

    def add(self,x):
        if self.heapSize == self.length:
            self.__arr.append(x)
            self.heapSize += 1
            self.length += 1
        else:
            self.__arr[self.heapSize] = x
            self.heapSize += 1

        #print("par min HEap")
        #self.printHeap()
        self.bottomUpHeapify(self.heapSize-1)
        #self.printHeap()

    def bottomUpHeapify(self,i):
        parent = int((i-1)/2)
        while parent >= 0:
            if self.__arr[parent] > self.__arr[i]:
                self.__arr[parent],self.__arr[i]  = self.__arr[i],self.__arr[parent]
                i = parent
                parent = int((i-1)/2)
            else:
                break

    def topDownHeapify(self,i):
        left = 2*i + 1
        right = 2*i + 2

        while right < self.heapSize:
            if self.__arr[left] < self.__arr[i]:
                smallest = left
            else:
                smallest = i

            if self.__arr[right] < self.__arr[smallest]:
                smallest = right

            if smallest != i:
                self.__arr[i],self.__arr[smallest] = self.__arr[smallest],self.__arr[i]
                i = smallest
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break

        if left<self.heapSize and self.__arr[left] < self.__arr[i]:
            self.__arr[i],self.__arr[left] = self.__arr[left],self.__arr[i]

class MaxHeap:
    __arr = list()
    heapSize = 0
    length = 0

    def __init__(self,arr):
        self.__arr = arr
        self.heapSize = len(arr)
        self.length = self.heapSize

    def getMax(self):
        return self.__arr[0]

    def deleteMax(self):
        temp = self.__arr[0]
        self.__arr[self.heapSize - 1], self.__arr[0] = self.__arr[0], self.__arr[self.heapSize - 1]
        self.heapSize -= 1
        self.topDownHeapify(0)
        return temp

    def printArr(self):
        for ele in self.__arr:
            print(ele,end=" ")
        print()

    def printHeap(self):
        for i in range(self.heapSize):
            print(self.__arr[i],end=" ")
        print()

    def buildMaxHeap(self):
        for i in range(int(self.heapSize/2),-1,-1):
            self.topDownHeapify(i)

    def add(self,x):
        if self.heapSize == self.length:
            self.__arr.append(x)
            self.heapSize += 1
            self.length += 1
        else:
            self.__arr[self.heapSize] = x
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

class Median:
    __minH = MinHeap([])
    __maxH = MaxHeap([])

    def __init__(self):
        self.length = 0

    def add(self,x):
        if self.__maxH.heapSize == 0:
            self.__maxH.add(x)
        else:
            if self.length % 2 == 0:
                if self.__maxH.getMax() >= x:
                    self.__maxH.add(x)
                else:
                    self.__minH.add(x)
                    ele = self.__minH.deleteMin()
                    self.__maxH.add(ele)
            else:
                if self.__maxH.getMax() >= x:
                    self.__maxH.add(x)
                    ele = self.__maxH.deleteMax()
                    self.__minH.add(ele)
                else:
                    self.__minH.add(x)
        self.length += 1

        #print("MAx HEap:")
        #self.__maxH.printHeap()
        #print("Min HEap:")
        #self.__minH.printHeap()

    def getMedian(self):
        return self.__maxH.getMax()

    def deleteMedian(self):
        if self.length % 2 == 0:
            temp = self.__maxH.deleteMax()
            temp = self.__minH.deleteMin()
            self.__maxH.add(temp)
        else:
            self.__maxH.deleteMax()
        self.length -= 1

inp = int(input())
arr = [random.randint(0,100) for i in range(inp)]
#arr = [6,13,72,63,95]
#print(arr)
now = time.time()*1000
h1 = Median()
for ele in arr:
    h1.add(ele)
#print(h1.getMedian())
then = time.time()*1000
milliSec = int(round(then-now))
print(milliSec)