from collections import deque
import time
import threading

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
    
    def placeOrder(self,orders):
        for order in orders:
            print("Order placed:",order)
            self.enq(order)
            time.sleep(0.5)

    def serveOrder(self):
        while not self.isEmpty():
            print("Order served:",self.deq())
            time.sleep(1)
    
if __name__ == '__main__':
    q = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']

    t = time.time()

    t1 = threading.Thread(target=q.placeOrder, args=(orders,))
    t2 = threading.Thread(target=q.serveOrder)

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    print("done in:",time.time()-t)
