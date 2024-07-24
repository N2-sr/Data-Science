class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data,None,cur)

    def printForward(self):
        if self.head == None:
            print("List is Empty")
        else:
            cur = self.head
            while cur:
                print(cur.data,end="-->")
                cur = cur.next
        print()
    
    def printReverse(self):
        if self.head == None:
            print("List is Empty")
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            while cur:
                print(cur.data,end="-->")
                cur = cur.prev
        print()

if __name__ == '__main__':
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.append(60)

    ll.printForward()
    ll.printReverse()
