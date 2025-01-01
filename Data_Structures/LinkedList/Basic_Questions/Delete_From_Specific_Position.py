class Node:
    def __init__(self, data):
        self.data = data
        self.addr = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.addr is not None:
                temp = temp.addr
            temp.addr = new_node
    def deleteFromSpecificPosition(self, position):
        if self.head is None:
            print("List is empty, nothing to delete.")
        if position == 1:
            temp = self.head
            self.head = self.head.addr
            del temp
        temp = self.head
        prev = None
        for i in range(1, position):
            prev = temp
            temp = temp.addr
            if temp is None:
                print("Position out of range.")
        prev.addr = temp.addr
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
ll.deleteFromSpecificPosition(3)
ll.display()
