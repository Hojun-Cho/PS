class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        filled,next  = 0,0
        while next < length:
            while next < length-1 and  nums[next] == nums[next+1]:
                next+=1
            nums[filled]= nums[next]
            filled+=1 
            next+=1
        return filled
      
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 0번 인덱스에는 값이 이미 차 있다고 가정하자
        filled,next = 0,0 
        # j는 항상 i보다 크다 
        while next < len(nums):
            # 중복을 건너뛴다
            if nums[filled] == nums[next]:
                next+=1
            # 현재 next에는 중복되지 않은 값이 들어있다.
            # i+1에 값을 넣는 이유는 i는 이미 값이 filled
            else :
                nums[filled+1] = nums[next]
                filled+=1 
        return filled + 1 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        duplicated_count = 0
        for i in range(1,length):
            if nums[i] == nums[i-1]:
                duplicated_count +=1
            else :
                # i - duplicated_count 는 값을 채워야 할 index
                nums[i-duplicated_count] = nums[i]
        return length - duplicated_count
