class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def printTree(self,n=0):
        print("   "*n, end="")
        print("|--",self.data)
        if self.children:
            for child in self.children:
                child.printTree(n+1)
            

def buildTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("GalaxyBook"))
    laptop.addChild(TreeNode("ThinkPad"))
    
    mobile = TreeNode("Mobile")
    mobile.addChild(TreeNode("Samsung"))
    mobile.addChild(TreeNode("Iphone"))
    mobile.addChild(TreeNode("Google Pixel"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("Xiaomi"))


    root.addChild(laptop)
    root.addChild(mobile)
    root.addChild(tv)

    return root

if __name__ == '__main__':
    root = buildTree()
    root.printTree()
