#!/usr/bin/env python3

def mergeSort(arr: list[int]) -> list[int]:
    """Merge sort algorithm"""
    n: int = len(arr)
    if n <= 1:
        return arr
    
    m: int = n // 2
    l_arr: list[int] = arr[:m]
    r_arr: list[int] = arr[m:]
    mergeSort(arr= l_arr)
    mergeSort(arr= r_arr)
    
    i: int = 0 # merged list index
    j: int = 0 # l_arr index
    k: int = 0 # r_arr index

    while j < m and k < n-m:
        if l_arr[j] <= r_arr[k]:
            arr[i] = l_arr[j]
            j+=1
        else:
            arr[i] = r_arr[k]
            k+=1
        
        i+=1

    while j < m:
        arr[i] = l_arr[j]
    
        i+=1
        j+=1
    
    while k < n-m:
        arr[i] = r_arr[k]
    
        i+=1
        k+=1

    return arr

if __name__ == "__main__":
    sorted_list = mergeSort(arr= [56,45,25,5,35,24,2,6,10,32])
    
    print(sorted_list)