class Node:
    def __init__(self, data):
        self.data = data
        self.addr = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        print("Linked List elements:", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.addr
        print()

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.addr is not None:
                temp = temp.addr
            temp.addr = new_node

    def DeleteFromBeginning(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
        else:
            temp = self.head
            self.head = self.head.addr
ll=LinkedList()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtEnd(40)
ll.display()
ll.DeleteFromBeginning()
ll.DeleteFromBeginning()
ll.display()
