def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                tem=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tem
    return arr
