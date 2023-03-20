class Tree:
    def __init__(self) -> None:
        self.data = ''
        self.leftPtr = None
        self.rightPtr = None

class BinaryTree:
    def __init__(self) -> None:
        self.rootPtr = None
        self.freePtr = 0
        self.size = 10
        self.treeList = [Tree() for x in range(self.size)]

    def initialiseTree(self):
        for x in range(self.size - 1):
            self.treeList[x].leftPtr = x+1
        self.treeList[self.size - 1].leftPtr = None

    def addNode(self, item):
        # check if free pointer in not None
        if self.freePtr != None:
            newNodePtr = self.freePtr
            self.freePtr = self.treeList[newNodePtr].leftPtr
            self.treeList[newNodePtr].data = item
            self.treeList[newNodePtr].leftPtr = None
            self.treeList[newNodePtr].rightPtr = None

            # check if first node
            if self.rootPtr == None:
                self.rootPtr = newNodePtr

            # else find insertion point
            else:
                thisPtr = self.rootPtr
                prevPtr = None
                turnedLeft = True

                while thisPtr is not None:
                    prevPtr = thisPtr

                    if item < self.treeList[thisPtr].data:
                        turnedLeft = True
                        thisPtr = self.treeList[thisPtr].leftPtr
                    else:
                        turnedLeft = False
                        thisPtr = self.treeList[thisPtr].rightPtr

                if turnedLeft:
                    self.treeList[prevPtr].leftPtr = newNodePtr
                else:
                    self.treeList[prevPtr].rightPtr = newNodePtr


    def findNode(self, item):
        thisPtr = self.rootPtr;

        while thisPtr is not None and self.treeList[thisPtr].data != item:
            if item < self.treeList[thisPtr].data:
                thisPtr = self.treeList[thisPtr].leftPtr
            else:
                thisPtr = self.treeList[thisPtr].rightPtr

        return thisPtr

    
    def traversal(self, RootPtr = 0):
        if self.treeList[RootPtr].leftPtr != None:
            self.traversal(self.treeList[RootPtr].leftPtr)
        
        print(str(self.treeList[RootPtr].data))

        if self.treeList[RootPtr].rightPtr != None:
            self.traversal(self.treeList[RootPtr].rightPtr)

    def displayTree(self):
        for i in range(self.size):
            print(f"Index: {i} | Left Ptr: {self.treeList[i].leftPtr} | Data: {self.treeList[i].data} | Right Ptr: {self.treeList[i].rightPtr}")

tree = BinaryTree()
tree.initialiseTree()

tree.addNode("D")
tree.addNode("B")
tree.addNode("A")
tree.addNode("F")
tree.addNode("C")

tree.displayTree()
print("============================== \n")

print(f"Searched Node Index: ", tree.findNode("C"))

print("============================== \n")

tree.traversal()