class Node:
    def __init__ (self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    # insert

    def insert(self,data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # print

    def printL(self):
        current = self.head
        while(current):
            print(current.data, end = " ")
            current = current.next
            print()

    #Deleting Node

    def deleteNode(self, a):
            current = self.head
            while(current.next):
                if current.data == a:
                    if current == self.head:
                        self.head = current.next
                        del current
                        break
                    elif current.next == None:
                        del current
                        break
                p = current
                current = current.next
            p.next = None
            del current

    #Finding Node

    def findByIndex(self,indexno):
        currentNode = self.head
        c = 0
        while True:
            if indexno == c:
                print("Data in index No.", indexno,":",currentNode.data)
                return
            elif currentNode.next is None :
                print('index has no Value')
                return
            else:
                currentNode = currentNode.next
                c += 1

    def findByData(self,element):
        current = self.head
        while current:
            if (current.data == element):
                print("Data exsist")
                return
            current = current.next
        print("Data don't, exsist")

    # inserting Node in Between
    def instapp(self,data,indexno):
        newNode = Node(data)
        current = self.head
        c = -1
        while current:
            if indexno == 0: #at index 0
                newNode.next = current
                self.head = newNode
                return
            elif indexno == c: # in b/w index
                newNode.next =  current.next
                current.next = newNode
                return
            elif current.next == None:   # last index
                current.next = newNode
                return
            current = current.next
            c += 1

            # sort

    def linkSort(self):
        

    # reverse

    def linkreverse(self):
        current = self.head
        nxt = None
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

LL = LinkedList()
n = int(input("Enter the total number of element you want to insert:"))
for i in range(n):
    print("Enter node",i+1,": ",end="")
    a = int(input())
    LL.insert(a)
LL.printL()
# LL.findByIndex(3)
# LL.findByData(4)
# LL.instapp(6,5)
# print("update")
# LL.printL()
LL.linkreverse()
print("reverse link list")
LL.printL()
