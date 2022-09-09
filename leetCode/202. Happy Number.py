# 토끼와 거북이 
# 사이클은 없지만 fast가 1 
# 19 -> 82 -> 68 -> 100 -> 1 
# 19 -> 68 -> 1
# 사이클이 존재  : 토끼와 거북이가 만난다면 사이클이 존재 
# 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 
# 58 -> 145 -> 20 -> 16 -> 58 -> 145 ->20-> 16 -> 58 
class Solution:
    def isHappy(self, n: int) -> bool:
        def squared(n)-> int:
            num = 0 
            while n != 0 :
                mod = n % 10 
                num+= (mod**2)
                n= n//10
            return num 
    
        slow = squared(n)
        fast = squared(squared(n))
        while slow != fast and fast != 1 :
            slow = squared(slow)
            fast = squared(squared(fast))
        return True if fast == 1 else False 
