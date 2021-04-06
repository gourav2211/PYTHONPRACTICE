class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def Push(self, x):

        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.size += 1
    
    def Pop(self):

        if (self.head == None):
            return 'Empty Stack'
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def Peek(self):
        if (self.head is None):
            return 'Empty Stack'
        return self.head.data
    
    def Size(self):
        return self.size
    
if __name__ == "__main__":
    ms = MyStack()
    print(ms.Pop())
    ms.Push(10)
    ms.Push(20)
    ms.Push(30)
    ms.Push('asn')
    print(ms.Pop())
    print(ms.Pop())
    print(ms.Peek())
    print(ms.Size())



