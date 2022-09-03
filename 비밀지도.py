from typing import List

def solution(n :int, arr1 :List[int], arr2: List[int]) -> int: 
    answer=[ bin(x|y)[2:].zfill(n) for x,y in zip(arr1,arr2)]
    return [ col.replace("1","#").replace("0"," ") for col in answer ]
