class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start,end = 0,length -1
        mid = 0
        while start <= end :
            mid = (start + end)//2
            if target == nums[mid]:
                return mid 
            if nums[mid] > target :
                end = mid -1 
            else :
                start = mid + 1
         # start에는 현재 target이 들어가는 index가 담겨있다
        return start
        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums :
            return nums.index(target)
        nums.append(target)
        nums.sort()
        return nums.index(target)
