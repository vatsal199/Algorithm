class KInversion:
    def __init__(self,arr,K):
        self.__arr = arr
        self.__k = K
        self.length = len(arr)

    def findDiffAtLeastK(self,low, high, X):
        index = -1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] >= X + K and arr[mid - 1] - X < self.__k:
                index = mid
                break
            elif arr[mid] >= X + K:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def partition(self,low, high):
        count = 0
        if low < high:
            mid = int((low + high) / 2)

            count += self.partition(low, mid)
            count += self.partition(mid + 1, high)
            count += self.merge(low, high)

        return count

    def merge(self,low, high):
        count = 0
        mid = int((low + high) / 2)
        p = low
        q = mid + 1
        temp = []
        while p <= mid and q <= high:
            if self.__arr[p] > self.__arr[q]:
                if self.__arr[p] - self.__arr[q] >= self.__k:
                    count += mid - p + 1
                else:
                    ind = self.findDiffAtLeastK(p + 1, mid, self.__arr[q])
                    if ind != -1:
                        count += mid - ind + 1
                        p = ind
                    else:
                        p = mid + 1
                temp.append(self.__arr[q])
                q += 1
            else:
                temp.append(self.__arr[p])
                p += 1

        while q <= high:
            temp.append(self.__arr[q])
            q += 1

        while p <= mid:
            temp.append(self.__arr[p])
            p += 1

        for i in temp:
            self.__arr[low] = i
            low += 1

        return count

    def findInversion(self):
        return self.partition(0,self.length-1)


arr = [6,4,2,1]
K = 2
k1 = KInversion(arr,K)
count = k1.findInversion()
print(count)