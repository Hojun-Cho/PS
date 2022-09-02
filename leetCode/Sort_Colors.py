# 그냥 정렬...
import numbers
from typing import List


class Solution:
    def sort(self,nums: List[int],low,high: numbers) -> None:
        if low >= high :
            return 
        mid = self.partition(nums,low,high)
        self.sort(nums,low,mid-1)
        self.sort(nums,mid,high)
    def partition(self,nums: List[int], low,high: numbers) -> numbers:
        pivot = nums[(low+high)//2]
        while low <= high:
                while nums[low] < pivot :
                    low += 1
                while nums[high] > pivot:
                    high -= 1
                if low <= high :
                    nums[high],nums[low] = nums[low],nums[high]
                    low,high = low +1 , high -1 
            # low를 기준으로 좌,우 값이 나뉜다.
        return low

    def sortColors(self, nums: List[int]) -> None:
        self.sort(nums,0,len(nums)-1) 
      
# 규칙이 존재 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # r,w는 index 0 부터 시작, blue는 index 거꾸로 시작
        red,white,blue = 0,0,len(nums)-1
        # white 가 blue 까지 도달해야 정렬이 되었다고 할 수 있다. 
        while white <= blue : 
            if nums[white] == 0 :
                nums[red],nums[white] = nums[white],nums[red]
                red , white = red+1,white+1
            elif nums[white] == 1 :
                white += 1
            # nums[white] == blue
            else :
                nums[white],nums[blue] = nums[blue],nums[white]
                # nums[blue] 에서 온 값이 무엇인지 모르기 때문에 blue만 -1
                blue-=1



        self.sort(nums,0,len(nums)-1) 
