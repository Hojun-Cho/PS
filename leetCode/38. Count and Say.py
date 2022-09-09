class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return "1"
        last_str = self.countAndSay(n-1) 
        length = len(last_str)
        count = 1 
        index = 0
        curr = ""
        while index < length:
            if index + 1 == length or last_str[index] !=last_str[index+1] :
                curr +=str(count)
                curr +=last_str[index]
                count =1 
            else :
                count +=1 
            index+=1
        
        return curr
