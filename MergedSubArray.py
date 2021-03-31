import MergeSortedList

class MergeSorting():

    def Merging(self, arr, low, mid, high):
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]

        i = 0
        j = 0
        k = low

        while (i < len(left) and j < len(right)):
            if (left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
                k += 1

            else:
                arr[k] = right[j]
                j += 1
                k += 1
        while (i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1
        while (j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1

    def MergeSort(self, arr, low, high):
        
        mid = (low + high) // 2
        if (high > low):
            self.MergeSort(arr, low, mid)
            self.MergeSort(arr,mid+1 ,high)

            self.Merging(arr,low, mid, high)

if __name__ == "__main__":
    arr = [int(x) for x in input().strip().split()]

    MergeSorting().MergeSort(arr, 0, len(arr)-1)
    print(arr)