#dummy headed doubly circular linked list
class Node:
    def __init__(self, e, n ,p):
        self.element = e
        self.next = n
        self.prev = p
#Task-2        
class DoublyList:
#1
    def __init__(self, a = None):
        self.head = Node(None, None, None)
        self.head.next = self.head.prev = self.head
        tail = None
        for i in range(len(a)):
            newNode = Node(a[i], None, None)
            if (self.head.next == self.head):                
                newNode.next = self.head.next
                newNode.prev = self.head
                self.head.next = newNode
                newNode.next.prev = newNode
                tail = newNode
                
            else:
                tail.next = newNode
                newNode.prev = tail
                newNode.next = self.head
                self.head.prev = newNode
                tail = newNode
#2    
    def showList(self):
        n = self.head.next
        if n == self.head:
            print("Empty List")
        else:
            while n is not self.head:
                print(n.element)
                n = n.next
                
    def insert(self, newElement, index = None):
        n  = self.head.next
        while n is not self.head:
            if n.element == newElement:
                print("Key already exists")
                return
            n = n.next 
        newNode = Node(newElement, None, None)    
        if index == None:
            n = self.head.next
            while n.next is not self.head:
                n = n.next
            n.next = newNode
            newNode.prev = n
            self.head.prev = newNode
            newNode.next = self.head
        else:
            n = self.head.next
            c = 0
            while n is not self.head:
                c = c+1
                n = n.next
            if (index<0 or index>c):
                raise Exception("Invalid index")
            if index == 0:
                newNode.next = self.head.next
                newNode.next.prev = newNode
                self.head.next = newNode
                newNode.prev = self.head
            else:
                for i in range(index):
                    n = n.next
                newNode.next = n.next
                n.next.prev = newNode
                n.next = newNode
                newNode.prev = n
                
    def insertBefore(self, elem, newElement):
        n = self.head.next
        newNode = Node(newElement, None, None)
        while n is not self.head:
            if n.element == elem:
                n.prev.next = newNode
                newNode.prev = n.prev
                n.prev = newNode
                newNode.next = n
            n = n.next

lst1 = DoublyList([1,2,3,4])
lst1.showList()
print("-------------")
lst2 = DoublyList([2,6,9,12,3,5,10,4])

lst2.insertBefore(12, 50)
lst2.showList()