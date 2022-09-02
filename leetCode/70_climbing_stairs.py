# 피보나치 수열과 비슷한 문제 
# dp를 이용해도 풀 수 있지만 dp보다 효율적으로 풀린다 => 
class Solution:
    def climbStairs(self, n: int) -> int:
        firstCount,secondCount = 1,1
        for i in range(n-1) :
            nextCount = firstCount + secondCount 
            firstCount, secondCount = secondCount, nextCount
        return secondCount
