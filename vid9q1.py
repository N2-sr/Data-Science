class TreeNode:

    def __init__(self,name,desig):
        self.name = name
        self.desig = desig
        self.children = []
        self.parent = None
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def printName(self,n=0):
        print("   "*n, end="")
        print("|--",self.name)
        if self.children:
            for child in self.children:
                child.printName(n+1)

    def printDesig(self,n=0):
        print("   "*n, end="")
        print("|--",self.desig)
        if self.children:
            for child in self.children:
                child.printDesig(n+1)
    
    def printBoth(self,n=0):
        print("   "*n, end="")
        print(f"|-- {self.name} ({self.desig})")
        if self.children:
            for child in self.children:
                child.printBoth(n+1)

    def printTree(self, type):
        if type=="name":
            self.printName()
        elif type=="designation":
            self.printDesig()
        elif type=="both":
            self.printBoth()
            

def buildTree():
    root = TreeNode("Nihit","CEO")

    cto = TreeNode("Chinmay","CTO")
    root.addChild(cto)
    
    infraHead = TreeNode("Vishwa","Infrastructure Head")
    cto.addChild(infraHead)
    infraHead.addChild(TreeNode("Dhaval","Cloud Manager "))
    infraHead.addChild(TreeNode("Abhijit","App Manager "))
    
    appHead = TreeNode("Aamir","Application Head")
    cto.addChild(appHead)

    hrHead = TreeNode("Gels","HR Head")
    root.addChild(hrHead)
    hrHead.addChild(TreeNode("Peter","Recruitment Manager"))
    hrHead.addChild(TreeNode("Waqas","Policy Manager"))

    return root

if __name__ == '__main__':
    root = buildTree()
    root.printTree("name")
    print()
    root.printTree("designation")
    print()
    root.printTree("both")
