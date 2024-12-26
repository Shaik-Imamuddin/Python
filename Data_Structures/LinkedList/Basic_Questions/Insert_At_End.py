class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatEnd(self,data):     
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.addr is not None:
                temp = temp.addr
            temp.addr=new_node
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
ll=LinkedList()
ll.insertatEnd(10)
ll.insertatEnd(20)
ll.insertatEnd(30)
ll.insertatEnd(40)
ll.display()
