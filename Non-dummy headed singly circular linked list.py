# Non- dummy singly circular linked list

class Node:
    def __init__(self, e, n = None):
        self.element = e
        self.next = n
#------------------------


class MyList:
    def __init__(self, a=None):
        self.head = None
        for i in range(0, len(a)):
            newNode = Node(a[i], None)
            if (self.head == None):
                self.head = newNode
                self.head.next = self.head
                tail = newNode
            else:
                tail.next = newNode
                newNode.next = self.head
                tail = newNode
        print("done")

    def showList(self):
        n = self.head
        while n.next is not self.head:
            print(n.element)
            n = n.next
        print(n.element)
               
    
    def insert(self, elem, index = None):
        n = self.head
        newNode = Node(elem, None)
        if index == None:
            while n.next is not self.head:
                n = n.next
            n.next = newNode
            newNode.next = self.head
        elif index != None:
            count = 1
            while n.next is not self.head:
                count += 1
                n = n.next
            
            if (index<0 or index>count):
                raise Exception("Invalid index")
            if (index == 0):
                newNode.next = self.head
                self.head = newNode
            else:
                i = 1
                m = self.head
                while i<index:
                    m = m.next
                    i = i+1
                newNode.next = m.next
                m.next = newNode




lst1 = MyList([1,2,3,4,5])
lst1.showList()
print("--------")
#lst1.insert(10)
#lst1.showList()
#print("--------")
#lst1.insert(30, 4)
#lst1.showList()