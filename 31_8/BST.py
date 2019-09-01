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

class BST:

    def __init__(self,value):
        self.root = Node(value)

    def insert(self,value):
        tempNode = Node(value)
        parent  = self.root
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

    def delete(self,value):
        deleteNode = self.search(value)

        if deleteNode is not None:
            if deleteNode.left is None and deleteNode.right is None:
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = None
                else:
                    deleteParent.left = None

            elif deleteNode.left is None:
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = deleteNode.right
                else:
                    deleteParent.left = deleteNode.right

            elif deleteNode.right is None:
                deleteParent = deleteNode.parent
                if deleteParent.key < deleteNode.key:
                    deleteParent.right = deleteNode.left
                else:
                    deleteParent.left = deleteNode.left

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

                successor.left = deleteNode.left
                if flag:
                    successor.right = deleteNode.right

                if deleteParent.key < deleteNode.key:
                    deleteParent.right = successor
                else:
                    deleteParent.left = successor


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


b1 = BST(35)
b1.insert(40)
b1.insert(39)
b1.insert(45)
b1.insert(44)
b1.insert(46)
b1.inorder()
b1.delete(40)
b1.inorder()