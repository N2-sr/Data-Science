from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def reverseString(self,str):
        rev = ""
        for char in str:
            s.push(char)
        while not s.isEmpty():
            rev += s.pop()
        return rev
    
if __name__ == '__main__':
    s = Stack()
    str = input("Enter string: ")
    rev = s.reverseString(str)
    print(rev)