# python has in built function deque you can
# use import collections to use it, it already had function like
# append(),appendleft(), pop(), poplefy(), reverse().
# you can intialize by d = collections.deque([],42), where
# 42 is max length
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def push(self, element):
        if(self.size == 0):
            print('stack is full')
        else:
            self.queue.append(element)

    def pop(self):
        if self.queue == []:
            print('stack is empty')
        else:
            self.queue.pop(0)

    def isEmpty(self):
        if self.queue == []:
            print("True")
        else:
            print('False')

    def peek(self):
        if self.queue == []:
            print('stack is empty')
        else:
            print(self.queue[-1])

    def qprint(self):
        print(self.queue)
