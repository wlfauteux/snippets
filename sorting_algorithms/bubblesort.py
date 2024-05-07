#!/usr/bin/env python3

def bubbleSort(arr: list[int]) -> list[int]:
    """Bubble sorting algorithm"""
    n: int = len(arr)
    i: int = 0

    while i < n-1:
        j: int = i+1
        
        while j <= n-1:
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

            j+=1
        
        i+=1

    return list

if __name__ == "__main__":
    sorted_list = bubbleSort(arr= [56,45,25,5,35,24,2,6,10,32])

    print(sorted_list)
