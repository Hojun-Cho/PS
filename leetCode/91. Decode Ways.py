# dp를 이용한 풀이
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0 
        length = len(s)
        dp = [0 for i in range(length+1)]
        dp[0] = 1 
        dp[1] = 1 
        for i in range(2,length+1):
            if 0< int(s[i-1]) <= 26 :
                dp[i] += dp[i-1]
            if 10<= int(s[i-2:i]) <= 26 :
                dp[i] += dp[i-2]
        return dp[length]
      
# 시간 초과
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0 
        # 0~ 26 
        length = len(s)
        cant = [False] * length 
        def check(n):
            return n >0 and n <=26            
        def permutation(chosen):
            if chosen >= length :
                return 1
            order= int(s[chosen])
            if order == 0:
                return 0 
            answer = 0
            if check(order) :
                answer+= permutation(chosen+1)
            if chosen < length -1 :
                order = int(s[chosen:chosen+2])
                if check(order) :
                    answer+= permutation(chosen+2)
            return answer 
        return permutation(0)
        
