class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = sys.maxsize
        length = len(nums)
        if sum(nums[:3]) > target :
            return sum(nums[:3])
        if sum(nums[-3:]) < target:
            return sum(nums[-3:])
        for i in range(length-2):
            if i >0 and nums[i] == nums[i-1] :
                continue 
            left,right = i+1 ,length-1
            while left < right :
                curr = nums[i] + nums[left] + nums[right]
                if abs(target-answer) > abs(target-curr):
                    answer= curr 
                if curr > target :
                    right -=1 
                elif curr < target :
                    left +=1 
                else :
                    return target 
        return answer
