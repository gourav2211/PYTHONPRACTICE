class BinarySearch():
    def Search(self, arr, t):
        low = 0
        high = len(arr) - 1
        if (arr[low] > t or arr[high] < t):
            return -1
        else:
            count = 0
            while (low <= high):
                count += 1
                print(count)
                mid = int((low +high) / 2)
                if(arr[mid] > t):
                    high = mid - 1 
                elif(arr[mid] < t):
                    low = mid + 1
                elif(arr[mid] == t):
                    return 1
            return -1    

    def BinaryCounting(self, arr):
        low = 0
        high = len(arr) - 1
        if (arr[low] == 0):
            return -1
        while (low <= high):
            mid = int((low + high)/2)
            if (arr[mid] == 1):
                low = mid + 1
            elif (arr[mid] != 1):
                high = mid - 1
                mid = mid - 1
        return (mid + 1)



if __name__ == "__main__":
    T = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(BinarySearch().BinaryCounting(arr))