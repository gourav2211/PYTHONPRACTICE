class Solutuion:
    
    def ReverseArray(self, arr):
        n = len(arr) - 1
        for i in range(int(n/2)):
            arr[i], arr[n-i] = arr[n-i], arr[i]

        return arr

def main():
    
    arr = [int(x) for x in input().strip().split()]

    arr = Solutuion().ReverseArray(arr)

    for i in arr:
        print(i,end=" ")

if __name__ == "__main__":
    main()