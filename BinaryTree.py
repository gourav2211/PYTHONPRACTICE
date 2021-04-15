

class BinaryTree:

    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


    def InorderTraversal(self, root):

        if (root != None):

            self.InorderTraversal(root.left)
            print(root.key, end = " ")
            self.InorderTraversal(root.right)
        return
    
    def PreOrderTraversal(self, root):
        if (root != None):
            print(root.key)
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)
    
    def PostOrderTraversal(self, root):
        if (root != None):
            self.PostOrderTraversal(root.left)
            self.PostOrderTraversal(root.right)
            print(root.key)
    
    def SizeOfBinaryTree(self, root):
        count = 0
        if root != None:
            self.InorderTraversal(root.left)
            count += 1
            self.InorderTraversal(root.right)

        return count
    
    def Insert(self, k):
        
        if root is None:
            root.key = k

        if k < self.key:
            if self.left is None:
                self.left = BinaryTree(k)
            else:
                self.left.Insert(k)
        elif k > self.key:
            if self.right is None:
                self.right = BinaryTree(k)
            else:
                self.right.Insert(k)
        else:
            self.key = k   
    
    def FindMaximum(self, root):
        if root is None:
            return root
        while (root.right != None):
            root = root.right

        return root
    
    def FindMinimum(self, root):
        if root is None:
            return root
        while (root.left != None):
            root = root.left

        return root
    
    def DeleteNode(self, root, x):
        if root is None:
            return root
        
        elif (root.key < x):
            root.right = self.DeleteNode(root.right, x)
        
        elif (root.key > x):
            root.left = self.DeleteNode(root.left, x)
        
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.FindMinimum(root.right)
            root.key = temp.key
            root.right = self.DeleteNode(root.right, temp.key)

        return root

        

        

if __name__ == "__main__":
    root = BinaryTree(20)
    root.Insert(30)
    root.Insert(50)
    root.Insert(10)
    root.Insert(40)
    root.Insert(90)
    root.Insert(45)
    root.Insert(15)
    root.Insert(5)
    root.InorderTraversal(root)
    temp = root.FindMinimum(root)
    root.DeleteNode(root, 20)
    print('Delete Successful')
    root.InorderTraversal(root)
    