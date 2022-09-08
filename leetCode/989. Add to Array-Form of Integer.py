class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        answer = []
        carry = 0 
        while num or k or carry  : 
            x = carry
            if num :
                x+=num.pop()
            if k:
                k,mod=divmod(k,10)
                x += mod 
            carry,mod = divmod(x,10)
            answer.append(mod)
        return answer[::-1]
      
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1,-1,-1):
          # carry, 현재 위치의 값 
            k,num[i] = divmod(k+num[i],10)
            # if가 실행되면 k의 길이가 더 big
            # else가 실행되면 num의 길이가 더 big
        return [ int(s) for s in str(k) ] + num  if k else num
                
