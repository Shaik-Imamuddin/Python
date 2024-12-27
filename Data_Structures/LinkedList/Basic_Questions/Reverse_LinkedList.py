class Node:
    def __init__(self,data):
        self.data=data
        self.addr = None
class Linkedlist:
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
    def reverseLinkedlist(self):
        prev = None
        current = self.head
        while current:
            next_node = current.addr
            current.addr = prev
            prev = current
            current = next_node
        self.head = prev
    def dispaly(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
        print()
ll=Linkedlist()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtEnd(40)
ll.dispaly()
ll.reverseLinkedlist()
ll.dispaly()
