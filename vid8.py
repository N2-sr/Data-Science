from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self,data):
        self.q.appendleft(data)

    def deq(self):
        return self.q.pop()

    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.size() == 0
    
if __name__ == '__main__':
    q = Queue()
    q.enq(1)
    q.enq(2)
    q.enq(3)
    q.enq(4)
    q.enq(5)

    print(q.size())

    print(q.deq())
    print(q.deq())
    print(q.deq())
    print(q.deq())
    print(q.deq())

    print(q.isEmpty())