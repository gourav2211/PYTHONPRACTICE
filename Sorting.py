class Sorting():
    def BubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr
    
    def SelectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(i+1,n):
                if (arr[i] < arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]

        return arr
    
    def InsertionSort(self, arr):
        n = len(arr)

        for i in range(1, n):
            b = arr[i]
            j = i - 1
            while (j>= 0 and arr[j] > b):
                arr[j+1] = arr[j]
                j -= 1
            arr[j] = b
        return arr
            

if __name__ == "__main__":
    input1 = [int(x) for x in input().strip().split()]
<<<<<<< HEAD
    arr = Sorting().BubbleSort(input1)
    arr1 = Sorting().InsertionSort(input1)
    print("Bubble Sort is :", end = '')
    print(arr)
=======
    arr1 = Sorting().InsertionSort(input1)
>>>>>>> Module1
    print("Insertion Sort is :", end = '')
    print(arr1)
