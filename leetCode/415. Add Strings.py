class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        carry = 0 
        answer = ""
        while num1 or num2 or carry :
            n =carry 
            if num1 :
                n+= int(num1.pop())
            if num2 :
                n+= int(num2.pop())
            carry = n // 10
            answer += str(n%10)
        return answer[::-1]

# 리스트로 변환하고 reverse 하는 부분이 사라졌다
# 문자를 아스키번호로 
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1,n2 = 0 ,0 
        for i in num1 :
            n1 = n1 * 10 + (ord(i) - 48)
        for j in num2 :
            n2 = n2 * 10 + (ord(j) - 48 )
        return str(n1 + n2)
            
