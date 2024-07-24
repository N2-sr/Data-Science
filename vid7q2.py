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
    
    def isBalanced(self,str):
        for char in str:
            if char == '(' or char == '{' or char=='[':
                s.push(char)
            elif char == ')' or char == '}' or char==']':
                if(s.peek() == '(' and char==')'):
                    s.pop()
                elif(s.peek() == '{' and char=='}'):  
                    s.pop()
                elif(s.peek() == '[' and char==']'):
                    s.pop()
                else:
                    return False
        return True
    
if __name__ == '__main__':
    s = Stack()
    str = input("Enter string: ")
    res = s.isBalanced(str)
    print(res)