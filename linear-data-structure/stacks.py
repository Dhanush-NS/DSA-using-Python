#Stack is a linear data structure which follows LIFO (Last in first out) where the last element is added to the stack that elem is first one to be removed

#Types of stack
# 1. Static stack(array based)
# 2. Dynamic stack (linked list based)

# Operations of stack
# Push
# pop
# peek (top)
# isfull for (array based)
# isempty

# Static stack

class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = []
    def push(self,*item):
        if len(self.stack) < self.size:
            self.stack.append(item)
            print(f"pushed {item} into the stack")
        else:
            print("stack is overflow")
    def pop(self):
        #remove and return the top elemant 
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is underflow")
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("elements in the stack",self.stack[::-1])
s = Stack(10)
s.push(110,232,23,3)
print(s.pop())
print(s.peek())
s.display()