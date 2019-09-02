'''
Author: Dhameliya Vatsalkumar
Email: Dhameliya.Vatsalkumar@iiitb.org
'''

class CircularQueue:
    def __init__(self,maxsize):
        self.__rear = -1
        self.__front = -1
        self.__li = [-1]*maxsize
        self.__length = 0
        self.__size = maxsize

    def isEmpty(self):
        if self.__length == 0:
            return True
        else:
            return False

    def isAllSame(self):
        flag = True
        tempI = (self.__rear+1)%self.__size
        matchWith  = self.__li[tempI]
        tempI = (tempI + 1) % self.__size
        for i in range(1,self.__length):
            if self.__li[tempI] != matchWith:
                flag = False
                break
            tempI = (tempI + 1) % self.__size
        return flag


    def isFull(self):
        if self.__length == self.__size:
            return True
        else:
            return False

    def enqueue(self,value):
        if not self.isFull():
            self.__rear += 1
            self.__rear %= self.__size
            self.__li[self.__rear] = value
            self.__length += 1

    def dequeue(self):
        if not self.isEmpty():
            self.__front += 1
            self.__front %= self.__size
            self.__length -= 1
            return self.__li[self.__front]

    def top(self):
        return self.__li[self.__rear]


class Stack:

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
        self.height = 0


class AVL:
    def __init__(self,value):
        self.root = Node(value)

    def inorder(self):
        print("Inorder:",end=" ")
        s1 = Stack()
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

    def insert(self,value):
        tempNode = Node(value)
        parent  = self.root
        while parent is not None:
            parent.height += 1
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
        return tempNode

    def updateHeight(self,x):
        if x.right is not None and x.left is not None:
            x.height = max(x.left.height, x.right.height) + 1
        elif x.right is None and x.left is None:
            x.height = 0
        elif x.right is None:
            x.height = x.left.height + 1
        else:
            x.height = x.right.height + 1
			
    def setParentOfChild(self,tempParent):
        if tempParent.left is not None:
            tempParent.left.parent = tempParent

        if tempParent.right is not None:
            tempParent.right.parent = tempParent

    def zig_zig(self,gParent,q1):
        if q1.top() == 0:
            tempParent = gParent.left

            gParent.left = tempParent.right
            tempParent.right = gParent

            parentOfgp = gParent.parent
            gParent.parent = tempParent
            tempParent.parent = parentOfgp

            self.setParentOfChild(gParent)

            if parentOfgp is not None:
                if parentOfgp.right is not None and parentOfgp.right.key == gParent.key:
                    parentOfgp.right = tempParent
                else:
                    parentOfgp.left = tempParent

            self.updateHeight(gParent)
            return tempParent
        else:
            tempParent = gParent.right

            gParent.right = tempParent.left
            tempParent.left = gParent

            parentOfgp = gParent.parent
            gParent.parent = tempParent
            tempParent.parent = parentOfgp

            self.setParentOfChild(gParent)

            if parentOfgp is not None:
                if parentOfgp.right is not None and parentOfgp.right.key == gParent.key:
                    parentOfgp.right = tempParent
                else:
                    parentOfgp.left = tempParent

            self.updateHeight(gParent)
            return tempParent

    def zig_zag(self,gParent,q1):
        if q1.top() == 0:
            tempParent = gParent.left
            x = tempParent.right

            gParent.left = x.right
            tempParent.right = x.left

            parentOfgp = gParent.parent
            gParent.parent = x
            tempParent.parent = x
            x.parent = parentOfgp

            x.left = tempParent
            x.right = gParent

            self.setParentOfChild(tempParent)
            self.setParentOfChild(gParent)


            if parentOfgp is not None:
                if parentOfgp.right is not None and parentOfgp.right.key == gParent.key:
                    parentOfgp.right = x
                else:
                    parentOfgp.left = x


            self.updateHeight(x.left)
            self.updateHeight(x.right)
            return x

        else:
            tempParent = gParent.right
            x = tempParent.left
            gParent.right = x.left
            tempParent.left = x.right

            parentOfgp = gParent.parent
            gParent.parent = x
            tempParent.parent = x
            x.parent = parentOfgp

            x.left = gParent
            x.right = tempParent

            self.setParentOfChild(tempParent)
            self.setParentOfChild(gParent)

            if parentOfgp is not None:
                if parentOfgp.right is not None and parentOfgp.right.key == gParent.key:
                    parentOfgp.right = x
                else:
                    parentOfgp.left = x

            self.updateHeight(x.left)
            self.updateHeight(x.right)
            return x

    def findLeftRight(self,tempParent,child):
        if tempParent.right is None:
            return 0
        elif tempParent.left is None:
            return 1
        elif tempParent.right.key == child.key:
            return 1
        else:
            return 0

    def correctBalanceFactor(self,insertedNode):
        tempParent = insertedNode.parent
        gParent = tempParent.parent

        if gParent is None:
            return tempParent

        q1 = CircularQueue(2)

        lr = self.findLeftRight(tempParent,insertedNode)
        q1.enqueue(lr)

        lr = self.findLeftRight(gParent, tempParent)
        q1.enqueue(lr)

        while gParent is not None:
            balanceFactor = 0
            if q1.top() == 1 and gParent.left is not None:
                # (left+1)-(right+1)
                balanceFactor = abs(gParent.left.height - gParent.right.height)
            elif q1.top() == 0 and gParent.right is not None:
                balanceFactor = abs(gParent.left.height - gParent.right.height)
            elif q1.top() == 1 and gParent.left is None:
                balanceFactor = gParent.right.height + 1
            else:
                balanceFactor = gParent.left.height + 1


            if balanceFactor > 1:
                if q1.isAllSame():
                    gParent = self.zig_zig(gParent,q1)
                else:
                    gParent = self.zig_zag(gParent,q1)

            self.updateHeight(gParent)

            tempParent = gParent
            gParent = gParent.parent

            if gParent is None:
                return tempParent

            q1.dequeue()
            lr = self.findLeftRight(gParent, tempParent)
            q1.enqueue(lr)


    def insertNode(self,value):
        insertedNode = self.insert(value)
        self.root = self.correctBalanceFactor(insertedNode)


a1 = AVL(10)
a1.insertNode(5)
a1.insertNode(2)
a1.insertNode(15)
a1.insertNode(20)
a1.insertNode(11)
a1.insertNode(14)
a1.insertNode(12)
a1.inorder()