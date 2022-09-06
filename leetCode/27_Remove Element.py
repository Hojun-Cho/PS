class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        filled = length-1
        answer = length
        for i,n in enumerate(nums):
            if i == filled and n == val:
                answer-=1
            elif i < filled and n == val :
                while i  < filled and  nums[filled] == val :
                    answer -= 1
                    filled-=1 
                nums[filled] ,nums[i] = nums[i],nums[filled]
                answer -=1 
                filled -=1 
        return answer
      
 class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      # 문제에서 val 값만 제거하라고 했음, 따라서 위치를 모두 교환 필요 x 
      # val_index는  현재 배열에서 가장 처음에 있는 val의 index를 가르킨다.
        val_index = 0
        for n in nums:
            if n != val :
                nums[val_index] = n 
                val_index +=1
        return val_index
