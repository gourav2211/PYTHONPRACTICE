class Sorting():

    def LumotoPartition(self, arr, low, high):
        
        pivot = arr[high]
        i = low -1
        for j in range(low, high):
            if (arr[j] < pivot):
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1

    def QuickSort(self, arr, low, high):
        if (low < high):

            pivot = self.LumotoPartition(arr,low,high)
            self.QuickSort(arr,low,pivot-1)
            self.QuickSort(arr, pivot+1, high)




if __name__ =="__main__":
    arr = [int(x ) for x in input().strip().split()]
    Sorting().QuickSort(arr, 0, len(arr)-1)
    print(arr)