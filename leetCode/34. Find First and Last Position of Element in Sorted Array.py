from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        left,right = 0,length-1 
        l = inf 
        while left<= right:
            mid = (left+right)//2
            if nums[mid] > target :
                right = mid -1 
            elif nums[mid] < target : 
                left = mid +1
            else :
                right = mid -1
                l = mid 
        if l == inf :
            return [-1,-1]
        r = 0 
        for i in range(l,length):
            if nums[i] != target:
                break
            r = i  
        return [l,r]
