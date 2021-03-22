class MyHash:
    def __init__(self):
        self.size = 0
        self.hash = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.key = 0
        self.size

    def HashFunction(self, val):
        self.key = val % 13
        return self.key
    def AddElements(self, val):
        search_res = self.SearchElements(val)
        if search_res == True:
            return 'Value Already present'
        else:

            key = self.HashFunction(val)
            self.hash[key].append(val)
            self.size += 1
            return 'Insert Operation successful'
    def DeleteElements(self, val):
        self.key = self.HashFunction(val)
        if (val in self.hash[self.key]):
            self.hash[self.key].remove(val)
            self.size -= 1
            return 'Item Deleted'
        else:
            return 'Item not found'
    def SearchElements(self,val):
        self.key = self.HashFunction(val)
        if (len(self.hash) == 0): 
            return False
        else:
            if (len(self.hash[self.key]) == 0):
                return False
            else:

                if (val in self.hash[self.key]):
                    return True
                else:
                    return False

if __name__ == '__main__':
    obj1 = MyHash()
    obj1.AddElements(20)
    obj1.AddElements(7)
    print(obj1.DeleteElements(20))
    x1 = obj1.SearchElements(20)
    print(x1)
    print(obj1.size)
        

