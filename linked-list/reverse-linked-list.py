# Problem Statement: Given the head of a singly linked list. Reverse the given linked list and return the head of the modified list.

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

def reverseLL(head):
    curr = head 
    prev = None 

    while curr:
        nextNode = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nextNode
    
    return prev 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reverseHead = reverseLL(head)

while reverseHead:
    print(reverseHead.val)
    reverseHead = reverseHead.next 