from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self,data):
        self.q.append(data)

    def deq(self):
        return self.q.popleft()

    def front(self):
        return self.q[0]
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.size() == 0
    
    def binaryNum(self,n):
        result = []
        self.enq("1")

        while n > 0:
            front = self.front()
            result.append(front)
            self.deq()
            self.enq(front + "0")
            self.enq(front + "1")
            n -= 1

        return result
    
if __name__ == '__main__':
    q = Queue()

    bin = q.binaryNum(10)

    print(bin)