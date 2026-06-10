#LinkedList calculations

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def count(self):
        cnt=0
        temp=self.head
        while temp:
            cnt+=1
            temp=temp.next
        print(cnt)
    def esum(self):
        temp=self.head
        sum=0
        while temp:
            if(temp.data%2==0):
                sum+=temp.data
            temp=temp.next
        print(sum)


l1=LinkedList()
l1.append(10)
l1.append(12)
l1.append(9)
l1.append(5)
l1.display()
l1.count()
l1.esum()
