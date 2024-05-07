#!/usr/bin/env python3

def quicksort(arr: list[int]) -> list[int]:
    """Quicksort algorithm"""
    n: int = len(arr)
    if n <= 1:
        return arr
    
    pivot: int = arr[0]
    L1: list[int] = []
    L2: list[int] = []

    i: int = 1

    while i < n:
        if arr[i] < pivot: L1.append(arr[i])
        else: L2.append(arr[i])

        i+=1
    
    return quicksort(arr= L1) + [arr[0]] + quicksort(arr= L2)

if __name__ == "__main__":
    sorted_list = quicksort(arr= [56,45,25,5,35,24,2,6,10,32])
    
    print(sorted_list)