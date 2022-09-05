class Solution:
    def reverse(self, x: int) -> int:
        answer = 0 
        # x의 부호를 저장 , x에 abs를 취해야 하는데 만약 x < 0 이면 (x % 10) 의도하지 않은 값이 나오기 때문에 abs로 양수로 만든다
        sign = 1 if x > 0 else -1
        x = abs(x)
        # 양수로 만든 x를 뒤집는다
        while True:
            answer +=(x % 10) 
            x //= 10
            if x == 0 :
                break 
            answer *= 10 
        answer *= sign
        if answer  < -2 **31 or answer  > (2**31) -1 :
            return 0 
        # 원래 부호를 곱한다
        return answer
    
class Solution:
    def reverse(self, x: int) -> int:
        answer = 0 
        # x의 부호를 저장 , x에 abs를 취해야 하는데 만약 x < 0 이면 (x % 10) 의도하지 않은 값이 나오기 때문에 abs로 양수로 만든다
        sign = 1 if x > 0 else -1
        x *= sign
        while x:
            answer = answer*10 + x % 10 
            x //= 10
        if answer  > (2**31) -1 :
            return 0 
        return answer * sign 
