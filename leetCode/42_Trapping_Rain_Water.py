from typing import List

# 경계를 설정하는 이유 : 현재 위치까지의 높이들 중 최댓값을 알아야지 얼마나 빗물을 담을지 알 수 있다.
class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left, right  = 0,len(height)-1
        # 각각 left,rihgt 까지의 최대 높이 , 이 높이를 이용해서 현재 left,right를 이동하며 답을 찾는다
        left_max, right_max = height[left], height[right]

        while left < right :
            left_max = max(height[left], left_max)
            right_max = max(height[right],right_max
            if left_max <= right_max :
                # 여기서 우측의 값을 고려하지 않는 이유는 현재 상황(left_max <= right_max)에서 우측에는 항상 빗물을 담을 수 있는 상황만 존재하기 때문이다 , ex) [1,0,2] [1,0,1]
                answer += (left_max - height[left])
                left += 1
            else :
                answer += (right_max - height[right])
                right -= 1
        return answer 
        

Solution().trap( [0,1,0,2,1,0,1,3,2,1,2,1])
