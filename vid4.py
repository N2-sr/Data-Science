class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = temp

    def insAtBegin(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = Node(data,self.head)
            self.head = temp

    def insertValues(self,dataList):
        self.head = None
        for data in dataList:
            self.insAtEnd(data)

    def appendValues(self,dataList):
        for data in dataList:
            self.insAtEnd(data)

    def insAtIndex(self,index,data):
        if index<0 or index>self.lengthll():
            raise Exception ("Invalid Index")
        elif index == 0:
            self.insAtBegin(data)
        else:
            cur = self.head
            while index!=1:
                cur = cur.next
                index -= 1
            temp = Node(data,cur.next)
            cur.next = temp

    def delAtIndex(self,index):
        if index<0 or index>self.lengthll():
            raise Exception ("Invalid Index")
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            while index != 1:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
 

    def printll(self):
        if self.head is None:
            print("LL is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end="-->")
                cur = cur.next
            print()

    def lengthll(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length

if __name__=='__main__':
    ll = LinkedList()
    ll.insAtEnd(100)
    ll.insAtEnd(200)
    ll.insAtEnd(300)
    ll.insAtEnd(400)
    ll.insAtBegin(500)
    ll.insAtBegin(600)
    ll.printll()
    print("Length is:",ll.lengthll())
    
    ll.insAtIndex(0,"9564")
    ll.printll()

    ll.delAtIndex(4)
    ll.printll()


