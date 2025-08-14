class Node:
    def __init__(self, val):
        self.data = val
        self.addr = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertatbegining(self, val):
        newNode = Node(val)
        newNode.addr = self.head
        self.head = newNode

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.addr

ll = Linkedlist()

while True:
    val = int(input())
    if val == -1:
        break
    ll.insertatbegining(val)

ll.display()
