class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.addr is not None:
                temp = temp.addr
            temp.addr = new_node
    def DeleteAtEnd(self):
        if self.head is None:
            print("List is empty")
        elif self.head.addr is None:
            self.head = None
        else:
            temp = self.head
            while temp.addr.addr is not None:
                temp = temp.addr
            temp.addr = None
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
        print()    
ll=LinkedList()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtEnd(40)
ll.display()
ll.DeleteAtEnd()
ll.display()
