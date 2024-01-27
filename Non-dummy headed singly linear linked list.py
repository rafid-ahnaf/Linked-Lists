#non-dummy headed singly linear linked list


class Node:
    def __init__(self, e, n = None):
        self.element = e
        self.next = n
#------------------------


class MyList:
    def __init__(self, a=None):
        self.head = None
        tail = None
        if a == None:
            self.head = None
        elif isinstance(a, list):
            for i in range(0, len(a)):
                newNode = Node(a[i], None)
                if (self.head == None):
                    self.head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
        elif isinstance(a, MyList):
            self.head = None
            tail = None
            n = a.head
            while n is not None:
                newNode = Node(n.element, None)
                if (self.head==None):
                    self.head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                n = n.next

#--------------------------------------------  
#2
    def showList(self):
        n = self.head
        if n == None:
            print("Empty list")
        else:
            while n is not None:
                print(n.element)
                n = n.next
                
                
    def remove_multiple_of_five(self):
        n = self.head
        temp = None
        while n is not None:
            
            if (n==self.head and n.element%5==0):
                self.head = n.next  
                temp = n
            elif (n.element%5 != 0):
                temp = n
            elif (n.element%5 == 0):
                temp.next = n.next 
            n = n.next
    
    def printDuplicate(self):
        n = self.head
        foundDuplicate = False
        while n is not None:
            m = n.next
            while m is not None:
                if n.element == m.element:
                    print(n.element)
                    foundDuplicate = True
                    break
                m = m.next
            if foundDuplicate == True:
                break
            n = n.next


lst1 = MyList([5,6,35,10,12,90])
lst2 = MyList([10,20,30,40,50])
lst3 = MyList([11,21,3,43,51])
lst4 = MyList([6,4,15,2,3,4])
lst4.printDuplicate()

#lst2.remove_multiple_of_five()
#lst2.showList()