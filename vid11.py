class bstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self,data):
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = bstNode(data)
        
        elif data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = bstNode(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements
    
    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()

        return elements
    
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)

        return elements
    
    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self.data
        
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self.data
        
    def findSum(self):
        elements = self.inOrderTraversal()
        return sum(elements)
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            minVal = self.right.findMin()
            self.data = minVal
            self.right = self.right.delete(minVal)

if __name__ == '__main__':

    ele = [30, 20, 10, 15, 25, 23, 39, 35, 42]

    root = bstNode(ele[0])
    for e in ele[1:]:
        root.addChild(e)

    print("Inorder:",root.inOrderTraversal())

    root.delete(20)

    print("Inorder:",root.inOrderTraversal())
    