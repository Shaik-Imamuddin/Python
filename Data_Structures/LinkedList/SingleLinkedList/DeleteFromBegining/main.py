class Node:
    def __init__(self,val):
        self.data=val
        self.addr=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatend(self,val):
        newNode=Node(val)

        if self.head is None:
            self.head=newNode
        else:
            temp = self.head
            while temp.addr is not None:
                temp=temp.addr
            temp.addr=newNode

    def deleteFromBegining(self):
        if self.head is None:
            print("Linkedlist is Empty,can't Delete")
            return
        temp = self.head
        self.head = self.head.addr
        del temp

    def display(self):
        if self.head is None:
            print("Linkedlist is Empty")
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr

ll=Linkedlist()
val=0

while True:
    val=int(input())
    if val==-1:
        break
    ll.insertatend(val)
ll.deleteFromBegining()
ll.display()