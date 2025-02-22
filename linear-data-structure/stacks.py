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
        # if size <= 0:
        #     raise ValueError("stack size must be greater than 0")
        self.stack = []
        self.size = size
    def isempty(self):
        return len(self.stack) == 0
            
        
    def isfull(self):
        return len(self.stack) == self.size
            
    def push(self,value):
        if self.isfull():
            raise ValueError("stack overflow")
        else:
            self.stack.append(value)
            print(f"Value {value} pushed into the stack")
    def pop(self):
        if self.isempty():
            raise ValueError("stack is empty")
        else:
            self.stack.pop()
            # print(f"value is removed")
    def display(self):
        if self.stack == 0:
            return "Stack is empty"
        return self.stack[::-1]
    def peek(self):
        return self.stack[-1]
    def reverse_str(self):
        string = "Dhanush"
        rev = ""
        for i in string:
            rev = i+rev
            
        return rev
try:
    s1 = Stack(10)
    print(s1.isempty())
    print(s1.isfull())
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.pop()
    print(s1.display())
    print(s1.peek())
    print(s1.reverse_str())
    
except ValueError as e:
    print("Error : ",e)




