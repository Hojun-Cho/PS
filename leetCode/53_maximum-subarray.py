from typing import List
# 그리디 
# 현재 -1 까지의 합이 >=0 이면 더한다 : 최적 
#                    <0 이면 더하지 않는다 : 최적

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int]  = [nums[0]]
        for i in range(1,len(nums)):
            sums.append(nums[i] +(sums[i-1] if sums[i-1]>= 0  else 0))
        return max(sums)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        current_sum = 0 
        for num in nums :
            current_sum = max(num,current_sum+num)
            max_sum = max(max_sum,current_sum)
        return max_sum
