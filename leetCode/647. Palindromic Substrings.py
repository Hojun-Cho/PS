# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0 
        length = len(s)
        # 인덱스가 i라고 가정하자
        # 우리는 [i,i]쌍과 [i,i+1] 쌍을 검사한다
        # i,i 는 홀수인 경우, i,i+1은 짝수인 경우를 검증한다
        # 인덱스 하나당 2번씩 반복되고 마지막 인덱스는 i+1을 할 수 없어서 2*length 에서 1을 뺀다
        for i in range(length*2-1):
            left = i//2
            right = i//2 + i%2 
            while left>=0 and right < length and s[left] == s[right] :
                result+=1
                left -=1
                right +=1 
        return result
     
# 2,3 슬라이딩 윈도우를 이용한 풀이 ,더 명확하다, 시간 복잡도는 동일 !!
class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(left: int,right: int)-> int:
            answer =0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                answer+=1
                left -=1
                right +=1
            return answer 
        answer=0
        for i in range(len(s)-1):
            answer+=check(i,i+1)
            answer+=check(i,i+2)
        return answer + len(s)
    
    
 # 비슷한 문제 https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length =  len(s)
        answer = ""
        for i in range(length * 2 -1) :
            left = i//2
            right = i//2 + i%2 
            while left >=0 and right < length and s[left] == s[right]:
                left -=1
                right +=1 
            answer = max(answer,s[left+1:right],key = len)
        return answer 
            
핵심은 홀수블럭과 짝수 블록을 생성하고 그 블럭을 기준올 좌우를 
