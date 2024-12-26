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
    def insertAtBegining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.addr = self.head
            self.head = new_node
    def dispaly(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
ll=Linkedlist()
ll.insertAtBegining(10)
ll.insertAtBegining(20)
ll.insertAtBegining(30)
ll.insertAtBegining(40)
ll.dispaly()
