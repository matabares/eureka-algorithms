# quick sort
import random


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if pivot >= arr[j]:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]  # wow! exchange
    arr[i + 1], arr[r] = arr[r], arr[i + 1]  # wow! exchange
    return i + 1


def quick_sort(arr,p,r):
    if(p<r):
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)


arr = list([random.randrange(1,10000000,1) for _ in range (999999)])
quick_sort(arr, 0, len(arr) - 1)
print(arr)
