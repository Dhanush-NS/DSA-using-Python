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
    def push(self,item):
        if len(self.stack) < self.size :
            self.stack.append(item)
            print(f"{item} is pushed into the stack")
        else:
            print("stack is overflow")
    def pop(self):
        #pop and return the item
        if not self.is_empty():
            print(self.stack.pop())
        else:
            print("stack is underflow")
            return None
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(f"top element",self.stack[-1])
    def is_empty(self):
        return len(self.stack) == 0
    def is_full(self):
        if self.is_full():
            print("stack is full")

    def display(self):
        """Print all elements of the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", self.stack[::])
s = Stack(10)
s.push(1)
s.push(10)
s.push(100)
s.push(1000)
s.display()
print(s.pop())
s.display()
s.peek()
s.display()
s.is_full()

