from StackImplementation import Node, MyStack

class ParenthesisChecker():
    def __init__(self):
        self.stack = MyStack()
    
    def ParenthesisChecker(self, data):
        for x in data:
            if x in ('[', '(', '{'):
                self.stack.Push(x)
            elif x in (')', ']', '}'):
                if x == ')':
                    if (self.stack.Peek() == '('):
                        self.stack.Pop()
                    else:
                        return 'Not balanced'
                if x == ']':
                    if (self.stack.Peek() == '['):
                        self.stack.Pop()
                    else:
                        return 'Not Balanced'
                if x == '}':
                    if (self.stack.Peek() == '{'):
                        self.stack.Pop()
                    else:
                        return 'Not Balanced'
        if self.stack.size == 0:
            return 'Balanced'
        else:
            return 'Not Balanced'
        
        
                


if __name__ == "__main__":
   ms = ParenthesisChecker()
   print(ms.ParenthesisChecker('abc())'))