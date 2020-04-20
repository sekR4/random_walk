class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        #Complete this method
        # To be honest, I don't see a use case for this task
        # I also don't understand what this code is doing here.
        newNode = Node(data)
        if head == None:
            return newNode
        else:
            pointer = head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = newNode
            return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
