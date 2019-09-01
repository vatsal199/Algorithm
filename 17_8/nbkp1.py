'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''
class Kstacks:
    # for given K it will crate K Stacks indexed 0,1,...,K-1
    def __init__(self,K):
        self.__K = K
        self.__stacks = [[] for i in range(0,K)]
        self.__lenStk = [0 for i in range(0,K)]

    def isithEmpty(self,i):
        if self.__lenStk[i] == 0:
            return True
        else:
            return False

    def printith(self,i):
        print(self.__stacks[i])

    def pushInith(self,i,X):
        self.__stacks[i].append(X)
        self.__lenStk[i] += 1

    def popFromith(self,i):
        if not self.isithEmpty(i):
            temp = self.__stacks[i][self.__lenStk[i]-1]
            self.__stacks[i].pop()
            self.__lenStk[i] -= 1
            return temp
        else:
            return -1

    def getTopFromith(self,i):
        if not self.isithEmpty(i):
            return self.__stacks[i][self.__lenStk[i]-1]
        else:
            return -1

    def getAllTops(self):
        li = list()
        for i in range(self.__K):
            if not self.isithEmpty(i):
                li.append(self.getTopFromith(i))
        return li

    def getEmptyi(self):
        index = -1
        for i in range(self.__K):
            if self.__lenStk[i] == 0:
                index = i
                break
        return index


class MoreThanK:
    def __init__(self,arr,K):
        self.__arr = arr
        self.length = len(arr)
        self.__K = K
        self.__k1=Kstacks(K-1)

    def findMejority(self):
        for i in range(self.length):
            flag = True
            for j in range(0,self.__K-1):
                if not self.__k1.isithEmpty(j) and self.__k1.getTopFromith(j) == self.__arr[i]:
                    self.__k1.pushInith(j,self.__arr[i])
                    flag = False
                    break

            if flag and self.__k1.getEmptyi() != -1:
                empty_i = self.__k1.getEmptyi()
                self.__k1.pushInith(empty_i,self.__arr[i])
                flag = False

            j = 0
            while flag and j<self.__K-1:
                temp = self.__k1.popFromith(j)
                j += 1

        mjrt = self.__k1.getAllTops()
        finalLi = list()
        for i in range(len(mjrt)):
            count = int(self.length/self.__K)+1
            for ele in self.__arr:
                if ele == mjrt[i]:
                    count -= 1
            if count < 1:
                finalLi.append(mjrt[i])

        return finalLi


arr = [1,3,1,1,2,2,2,2,2,3,3,3,3,2]
#arr = [1,2,3,3]
k = 3
m1 = MoreThanK(arr,k)
print(m1.findMejority())