class Solution():

    def sumN(self, n):
        if (n == 1):
            return 1
        else:
           return (n + self.sumN(n-1))

    def factorialN(self, n):
        if (n == 1):
            return 1
        else:
            return n*self.factorialN(n-1)
    def FibonacciSeries(self,n):
        if (n == 1 or n == 0):
            return n
        else:
           return self.FibonacciSeries(n-1) + self.FibonacciSeries(n-2)



if __name__ == "__main__":
    T= int(input())
    print(Solution().sumN(T))
    print(Solution().factorialN(T))
    for i in range(1,T+1):
        print(Solution().FibonacciSeries(i),end=", ")