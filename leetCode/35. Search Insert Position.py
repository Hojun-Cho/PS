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
         # start가 end를 넘어가면 end의 의미는 target보다 작은 값의 index
         # 그게 아니라면 end는 현재 target이 들어올 위치 
        return end+1 if start > end else end
        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums :
            return nums.index(target)
        nums.append(target)
        nums.sort()
        return nums.index(target)
