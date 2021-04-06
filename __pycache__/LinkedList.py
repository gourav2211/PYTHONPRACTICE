class LinkedList():

    def __init__(self, k):
        self.key = k
        self.next = None


l1 = LinkedList(10)
l1.next = LinkedList(20)
l1.next.next = LinkedList(30)

def displayList(head):
    if (head is None):
        return 
    
    else:
        curr = head
        while (curr != None):
            print(curr.key)
            curr = curr.next

displayList(l1)