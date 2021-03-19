class Solution:
    def RotateArray(self, arr, n):

        if (n < len(arr)):
            temp = []
            for i in range(n):
                temp.append(arr[0])
                del(arr[0])

            for j in temp:
                arr.append(j)
            return arr
        else:
            return 'Size not allowed'

def main():
    T = int(input())
    arr = [int(x) for x in input().strip().split()]

    x1 = Solution().RotateArray(arr, T)
    print(x1)

if __name__ == "__main__":
    main()
        
