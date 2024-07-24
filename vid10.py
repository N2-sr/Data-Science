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
    

if __name__ == '__main__':

    ele = [30, 20, 10, 15, 25, 23, 39, 35, 42]

    root = bstNode(ele[0])
    for e in ele[1:]:
        root.addChild(e)

    print(root.inOrderTraversal())