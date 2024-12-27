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
    def InsertAtPosition(self, pos, data):
        if pos == 0:
            self.InsertAtBegin(data)
        else:
            new_node = Node(data)
            temp = self.head
            for i in range(1, pos):
                if temp is None:
                    print("Invalid position")
                else:
                    temp = temp.addr
            if temp is None:
                print("Invalid position")
            else:
                new_node.addr = temp.addr
                temp.addr = new_node
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
ll.InsertAtPosition(2,40)
ll.InsertAtPosition(1,50)
ll.dispaly()
