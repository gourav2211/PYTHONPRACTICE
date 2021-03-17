class Solution:
    def InsertAtIndex(self, arr, size, index, element):
        arr.insert(index, element)


def main():
    T= int(input())
    while (T>0):
        size = int(input())
        arr = [int(x) for x in input().strip().split()]
        arr.append(-1)
        index, element = map(int, input().strip().split())
        Solution().InsertAtIndex(arr, size, index, element)

        for i in range(size):
            print(arr[i], end=" ")
        T -= 1
if __name__ == "__main__":
    main()