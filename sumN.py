# constant time
def fun1(n):
    return n*(n+1)/2

# O(n) time
def fun2(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
    