from LumotoPartition import Sorting

class Triangles(Sorting):

    def CountTriangles(self, arr):
        self.QuickSort(arr,0,len(arr)-1)
        n = len(arr)-1
        count = 0
        i = 0
        j = i + 1
        while (i < n-1):

            for k in range(j+1, n+1):
                if (arr[k] < arr[i] + arr[j]):
                    count += 1

            j = j+1

            if (j >= n):
                i += 1 
                j = i + 1
          
        return count
    
    def CountTriangles_Optimized(self, arr):
        arr.sort()
        count = 0
        n = len(arr)
        for i in range(n-2):
            k = i+2
            for j in range(i+1,n):

                while (k < n and arr[k] < arr[i] + arr[j]):
                    k += 1

                count += k-j-1
        
        return count






if __name__ == "__main__":
    T = [int(x) for x in input().strip().split()]
    t_count = Triangles().CountTriangles_Optimized(T)
    t_count1 = Triangles().CountTriangles(T)
    print("Optimized Quick Sort : ", t_count)
    print("Unoptimized Quick Sort : ", t_count1)
