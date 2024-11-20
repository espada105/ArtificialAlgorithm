def bubble_sort(arr):
    print("원시 배열\n--------------------\n",f"\n{arr}\n\n")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
        print(arr)

arr = [7,2,5,3,8,1]
bubble_sort(arr)
print(arr)