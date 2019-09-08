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
        self.prefixSum = value

class BST:

    def __init__(self,value):
        self.root = Node(value)

    def insert(self,value):
        tempNode = Node(value)
        parent  = self.root
        while parent is not None:
            if parent.key < value:
                tempNode.prefixSum = parent.prefixSum + value
                if parent.right is None:
                    tempNode.parent = parent
                    parent.right = tempNode
                    parent = None
                else:
                    parent = parent.right
            else:
                parent.prefixSum = parent.prefixSum + value
                if parent.right is not None:
                    self.inorderUpdate(parent.right,value)
                if parent.left is None:
                    tempNode.parent = parent
                    parent.left = tempNode
                    parent = None
                else:
                    parent = parent.left

    def inorder(self):
        print("Inorder Sum:",end=" ")
        s1 = stack()
        s1.push(self.root,True)

        while not s1.isEmpty():
            stackEntry = s1.pop()
            if stackEntry[1]:
                s1.push(stackEntry[0], False)
                if stackEntry[0].left is not None:
                    s1.push(stackEntry[0].left,True)
            else:
                '''print(stackEntry[0].key,end=" ")
                print("s:",stackEntry[0].prefixSum,end=" ")'''
                print(stackEntry[0].prefixSum, end=" ")
                if stackEntry[0].right is not None:
                    s1.push(stackEntry[0].right, True)

        print()

    def inorderUpdate(self,X,value):
        s1 = stack()
        s1.push(X,True)

        while not s1.isEmpty():
            stackEntry = s1.pop()
            if stackEntry[1]:
                s1.push(stackEntry[0], False)
                if stackEntry[0].left is not None:
                    s1.push(stackEntry[0].left,True)
            else:
                X.prefixSum += value
                if stackEntry[0].right is not None:
                    s1.push(stackEntry[0].right, True)


class PrefixSum:
    def __init__(self,arr):
        self.__b1 = BST(arr[0])
        for i in range(1,len(arr)):
            self.__b1.insert(arr[i])
        self.__b1.inorder()


arr = [25,13,12,16,14,15,75,50,98,60]
p1 = PrefixSum(arr)