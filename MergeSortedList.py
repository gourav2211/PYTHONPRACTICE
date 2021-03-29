class Sorting():
    def MergeList(self, arr1, arr2):
        arr3 = []
        counter_list1 = 0
        counter_list2 = 0

        while (len(arr1) != 0 and len(arr2) != 0):
            if (arr1[0] <= arr2[0]):
                arr3.append(arr1[0])
                counter_list1 += 1
                arr1.pop(0)
            else:
                arr3.append(arr2[0])
                counter_list2 += 1
                arr2.pop(0)

        if (len(arr1) == 0):
            for i in arr2:
                arr3.append(i)
        else:
            for i in arr1:
                arr3.append(i)
        
        return arr3

if __name__ == "__main__":
    arr1 = [int(x) for x in input().strip().split()]
    arr2 = [int(x) for x in input().strip().split()]
    print(arr1)
    print(arr2)
    merged_list = Sorting().MergeList(arr1, arr2)
    print("Merged List is :", end = " ")
    print(merged_list)
