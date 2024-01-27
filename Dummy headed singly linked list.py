#Dummy headed singly linked list

class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n
        
class DummySinglyList:

    def __init__(self, a = None):
        self.head = Node(None, None)
        tail = None
        for i in range(len(a)):
            newNode = Node(a[i], None)
            if (self.head.next == None):                               
                self.head.next = newNode               
                tail = newNode          
            else:
                tail.next = newNode                              
                tail = newNode
#2    
    def showList(self):
        n = self.head.next
        if n == None:
            print("Empty List")
        else:
            while n is not None:
                print(n.element)
                n = n.next   

    def sum(self, other):
        n = self.head.next
        m = other.head.next
        number1 = ""
        number2 = ""
        while n is not None:
            print(n.element)
            number1 += str(n.element)
            n = n.next
        while m is not None:
            print(m.element)
            number2 += str(m.element) 
            m = m.next
        result = str(int(number1)+int(number2))    
        print(result)
        nlist = []
        for i in result:
            nlist = nlist + [i]
        return DummySinglyList(nlist)
            
    
lst1 = DummySinglyList([4,5,3])
#lst1.showList()
lst2 = DummySinglyList([9,5,2])
lst4 = lst1.sum(lst2)
print("========")
lst4.showList()