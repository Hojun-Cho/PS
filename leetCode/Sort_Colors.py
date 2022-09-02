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
      
# red index : white의 첫 번째 항목을 가르킨다, 즉 항상 white의 첫 번째 요소 나타낸다
# white index : 현재 탐색중인 요소
# blue index : 자신의 인덱스 이후의 배열은 정렬된 상태임을 나타낸다
# white index가 red 이면 white index의 위치가 white의 첫 번째가 아니므로 red index를 +1, 그리고 다음 요소를 탐색하기 위해서 white index +1
# white index가 blue이면 white index의 값과 blue index의 값을 교체한다. 그리고 blue inde 에 -1을 더해주면 blue index 뒤까지는 모두 정렬된 상태가 된다  
# 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red,white,blue = 0,0,len(nums)-1
        while white <= blue : 
            if nums[white] == 0 :
                nums[red],nums[white] = nums[white],nums[red]
                red , white = red+1,white+1
            elif nums[white] == 1 :
                white += 1
            else :
                nums[white],nums[blue] = nums[blue],nums[white]
                blue-=1



        self.sort(nums,0,len(nums)-1) 
