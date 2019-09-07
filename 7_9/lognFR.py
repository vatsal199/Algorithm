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
        self.noOfNodes = 1

class BST:

    def __init__(self,value):
        self.root = Node(value)

    def insert(self,value):
        tempNode = Node(value)
        parent  = self.root
        while parent is not None:
            parent.noOfNodes += 1
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

    def search(self,value):
        parent = self.root
        while parent is not None:
            if parent.key == value:
                return parent
            elif parent.key < value:
                parent = parent.right
            else:
                parent = parent.left
        return None

    def bottomUpUpdate(self,X):
        while X is not None:
            X.noOfNodes -= 1
            X = X.parent

    def updatenoOfNodes(self,X):
        temp = 1
        if X.right is None and X.left is None:
            return temp
        elif X.right is None:
            temp = X.left.noOfNodes + 1
        elif X.left is None:
            temp = X.right.noOfNodes + 1
        else:
            temp = X.left.noOfNodes + X.right.noOfNodes + 1
        return temp

    def delete(self,value):
        deleteNode = self.search(value)

        if deleteNode is not None:
            if deleteNode.left is None and deleteNode.right is None:
                if deleteNode == self.root:
                    self.root = None
                    return
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = None
                else:
                    deleteParent.left = None
                self.bottomUpUpdate(deleteParent)

            elif deleteNode.left is None:
                if deleteNode == self.root:
                    self.root = deleteNode.right
                    return
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = deleteNode.right
                    deleteNode.right.parent = deleteParent
                else:
                    deleteParent.left = deleteNode.right
                    deleteNode.left.parent = deleteParent
                self.bottomUpUpdate(deleteParent)

            elif deleteNode.right is None:
                if deleteNode == self.root:
                    self.root = deleteNode.left
                    return
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = deleteNode.left
                    deleteNode.left.parent = deleteParent
                else:
                    deleteParent.left = deleteNode.left
                    deleteNode.right.parent = deleteParent
                self.bottomUpUpdate(deleteParent)

            else:
                deleteParent = deleteNode.parent
                successor = deleteNode.right
                flag = False
                while successor.left is not None:
                    flag = True
                    successor = successor.left

                successorParent = successor.parent
                if flag:
                    successorParent.left = successor.right
                    if successor.right is not None:
                        successor.right.parent = successorParent

                successor.left = deleteNode.left
                deleteNode.left.parent = successor

                if flag:
                    successor.right = deleteNode.right
                    if successor.right is not None:
                        successor.right.parent = successor

                if deleteParent.key < deleteNode.key:
                    deleteParent.right = successor
                else:
                    deleteParent.left = successor

                successor.parent = deleteParent
                if deleteNode == self.root:
                    self.root = successor
                successor.noOfNodes = self.updatenoOfNodes(successor)
                self.bottomUpUpdate(successorParent)


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
                if stackEntry[0].right is not None:
                    s1.push(stackEntry[0].right, True)

        print()

    def rank(self,key):
        tempRoot = self.root
        rank = 1
        flag = True
        while tempRoot is not None:
            if tempRoot.key == key:
                flag = False
                if tempRoot.right is not None:
                    rank += tempRoot.right.noOfNodes
                tempRoot = None
            elif tempRoot.key < key:
                tempRoot = tempRoot.right
            else:
                if tempRoot.right is not None:
                    rank += tempRoot.right.noOfNodes + 1
                else:
                    rank += 1
                tempRoot = tempRoot.left

        if flag:
            return -1
        else:
            return rank

    def findRank(self,rank):
        ele = -1
        tempRoot = self.root
        while tempRoot is not None and rank != 0:
            if tempRoot.right is not None:
                if rank == tempRoot.right.noOfNodes + 1:
                    ele = tempRoot.key
                    tempRoot = None
                elif tempRoot.noOfNodes == rank:
                    parent = tempRoot
                    tempRoot = tempRoot.left
                    while tempRoot is not None:
                        parent = tempRoot
                        tempRoot = tempRoot.left
                    ele = parent.key
                elif tempRoot.right.noOfNodes + 1 < rank:
                    rank -= tempRoot.right.noOfNodes + 1
                    tempRoot = tempRoot.left
                else:
                    tempRoot = tempRoot.right
            else:
                if rank == 1:
                    ele = tempRoot.key
                    tempRoot = None
                elif tempRoot.noOfNodes == rank:
                    parent = tempRoot
                    tempRoot = tempRoot.left
                    while tempRoot is not None:
                        parent = tempRoot
                        tempRoot = tempRoot.left
                    ele = parent.key
                elif 1 < rank:
                    rank -=  1
                    tempRoot = tempRoot.left
                else:
                    tempRoot = tempRoot.right
        return ele

class Rank:
    def __init__(self,arr):
        self.__b1 = BST(arr[0])
        for i in range(1,len(arr)):
            self.__b1.insert(arr[i])
        self.__b1.inorder()

    def rank(self,key):
        return self.__b1.rank(key)

    def findRank(self,rank):
        return self.__b1.findRank(rank)

arr = [25,13,12,16,14,15,75,50,98,60]
f1 = Rank(arr)
print(f1.rank(15))
print(f1.findRank(7))