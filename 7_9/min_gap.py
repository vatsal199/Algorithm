'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''

class stack:

    def __init__(self):
        self.__li = list()
        self.__length = 0

    def push(self,value,flag):
        self.__li.append([value,flag])
        self.__length += 1

    def getLength(self):
        return self.__length

    def isEmpty(self):
        if self.__length == 0:
            return True
        else:
            return False

    def pop(self):
        if not self.isEmpty():
            temp = self.__li[self.__length-1]
            self.__li.pop()
            self.__length -= 1
            return temp

class Node:

    def __init__(self,value):
        self.key = value
        self.parent = None
        self.right = None
        self.left = None
        self.minGap = 0

class BST:

    def __init__(self,value):
        self.root = Node(value)

    def insert(self,value):
        tempNode = Node(value)
        parent = self.root
        while parent is not None:
            if parent.key < value:
                if parent.right is None:
                    tempNode.parent = parent
                    parent.right = tempNode
                    parent = None
                else:
                    parent = parent.right
            else:
                if parent.left is None:
                    tempNode.parent = parent
                    parent.left = tempNode
                    parent = None
                else:
                    parent = parent.left

    def inorder(self):
        print("Inorder:",end=" ")
        s1 = stack()
        s1.push(self.root,True)

        while not s1.isEmpty():
            stackEntry = s1.pop()
            if stackEntry[1]:
                s1.push(stackEntry[0], False)
                if stackEntry[0].left is not None:
                    s1.push(stackEntry[0].left,True)
            else:
                print(stackEntry[0].key,end=" ")
                print("M:",stackEntry[0].minGap,end=" ")
                if stackEntry[0].right is not None:
                    s1.push(stackEntry[0].right, True)

        print()

    def inorderSuccesor(self,X):
        if X.right is not None:
            succ = X.right
            while succ.left is not None:
                succ = succ.left
            return succ
        else:
            succ = X.parent
            while succ is not None and succ.key < X.key:
                succ = succ.parent
            if succ is None:
                tempNode = Node(-1)
                return tempNode
            else:
                return succ

    def inorderPredeccesor(self,X):
        if X.left is not None:
            pred = X.left
            while pred.right is not None:
                pred = pred.right
            return pred
        else:
            pred = X.parent
            while pred is not None and pred.key > X.key:
                pred = pred.parent
            if pred is None:
                tempNode = Node(-1)
                return tempNode
            else:
                return pred



    def updateMinGap(self,X):
        succ = self.inorderSuccesor(X)
        pred = self.inorderPredeccesor(X)

        INT_MAX = 1000000
        smallestGap = INT_MAX

        if X.right is not None and smallestGap > X.right.minGap:
            smallestGap = X.right.minGap
        if X.left is not None and smallestGap > X.left.minGap:
            smallestGap = X.left.minGap
        if succ.key != -1 and smallestGap > abs(succ.key-X.key):
            smallestGap = abs(succ.key-X.key)
        if pred.key != -1 and smallestGap > abs(pred.key - X.key):
            smallestGap = abs(pred.key - X.key)

        if smallestGap == INT_MAX:
            return 0
        else:
            return int(smallestGap)


    def getMinGap(self):
        s1 = stack()
        s1.push(self.root,True)

        while not s1.isEmpty():
            stackEntry = s1.pop()
            if stackEntry[1]:
                s1.push(stackEntry[0], False)
                if stackEntry[0].right is not None:
                    s1.push(stackEntry[0].right,True)
                if stackEntry[0].left is not None:
                    s1.push(stackEntry[0].left,True)
            else:
                stackEntry[0].minGap = self.updateMinGap(stackEntry[0])

        return self.root.minGap


class Gap:
    def __init__(self,arr):
        self.__b1 = BST(arr[0])
        for i in range(1,len(arr)):
            self.__b1.insert(arr[i])
        #self.__b1.inorder()

    def getMinGap(self):
        return self.__b1.getMinGap()


arr = [25,13,12,16,14,15,75,50,98,60]
g1 = Gap(arr)
print("minGap:",g1.getMinGap())