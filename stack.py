class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = []

    def push(self,element):
        if self.size == 0:
            print('stack full')
        else:
            self.stack.append(element)
            self.size -= 1

    def pop(self):
        if(self.stack == [] ):
            print('stack is empty')
        else:
            self.stack.pop()
            self.size += 1

    def isEmpty(self):
        if self.stack == []:
            print('True')
        else:
            print('False')

    def peek(self):
        if self.size = []:
            print('stack is empty')
        else:
            print(self.stack[-1])

    def sprint(self):
        print(self.stack)
        
obj = Stack(10)
# obj.push(5)
# obj.sprint()
obj.pop()
