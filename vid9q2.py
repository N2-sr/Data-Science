class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def printTree(self,uptoLevel,currentLevel=0):
        print("   "*currentLevel, end="")
        print("|--",self.data)
        if self.children and currentLevel<uptoLevel:
            for child in self.children:
                child.printTree(uptoLevel,currentLevel+1)

def buildTree():
    root = TreeNode("Global")

    country1 = TreeNode("India")
    c1s1 = TreeNode("Gujarat")
    c1s2 = TreeNode("Karnataka")
    country2 = TreeNode("USA")
    c2s1 = TreeNode("New Jersey")
    c2s2 = TreeNode("California")

    root.addChild(country1)
    root.addChild(country2)

    country1.addChild(c1s1)
    country1.addChild(c1s2)
    c1s1.addChild(TreeNode("Ahmedabad"))
    c1s1.addChild(TreeNode("Baroda"))
    c1s2.addChild(TreeNode("Bangluru"))
    c1s2.addChild(TreeNode("Mysore"))


    country2.addChild(c2s1)
    country2.addChild(c2s2)
    c2s1.addChild(TreeNode("Princeton"))
    c2s1.addChild(TreeNode("trenton"))
    c2s2.addChild(TreeNode("San Francisco"))
    c2s2.addChild(TreeNode("Mountain View"))
    c2s2.addChild(TreeNode("Palo Alto"))

    return root

if __name__=='__main__':
    root = buildTree()
    root.printTree(1)
    print()
    root.printTree(2)
    print()
    root.printTree(3)
    print()