class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outs = [0] * len(nums)
        p = 1
        
        for i,num in enumerate(nums):
            outs[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums)-1,0-1,-1):
            outs[i] = outs[i] * p
            p *= nums[i]
        return outs 
            # 1 2 3 4 
            #1 1 2 6  
           
