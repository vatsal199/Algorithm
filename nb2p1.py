class MoreThanHalf:
    __arr = list()

    def __init__(self,arr):
        self.__arr = arr
        self.length = len(arr)

    def findX(self):
        count = 1
        max = arr[0]
        for i in range(1,self.length):
            if self.__arr[i] == max:
                count += 1
            elif count > 0:
                count -= 1
            else:
                count = 1
                max = self.__arr[i]

        count = 0
        for ele in self.__arr:
            if ele == max:
                count += 1
        if count > self.length/2:
            return max
        else:
            return -1


arr = [1,1,1,2,2,2,2,2,3,3,3,2,2]
h1 = MoreThanHalf(arr)
print(h1.findX())


