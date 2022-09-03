from typing import List

# 재귀 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0 :
            return []
        alphas = { "2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],
        "5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],
        "9":["w","x","y","z"]}
        answer :List[str]= []

        def perm(nowStr: str,index :int):
            if index == length :
                answer.append(nowStr)
                return
            for alpha in alphas[int(digits[index])] :
                perm(nowStr+alpha,index +1)
        perm("",0)
        return answer 
# 핵심은 전의 결과의 각각의 요소에(a,b,c 각각) 현재 문자들(d,e,f)을 더해주는 것. 다른 로직은 없다!
# 위의 풀이는 ["2","3"]일 경우 재귀를 총 12번 호출하지만 이렇게 요소마다 재귀를 호출하지 않으면 더 효율적 
# 밑에는 ["2","3"]일 경우 2번의 호출만 발생한다.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""
        alphas = { "2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],
        "5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],
        "9":["w","x","y","z"]}
        res = []
        def reduce(cur,acc):
            if cur == [] :
                return acc 
            now_res= [] 
            for s in cur :
                for a in acc : 
                    now_res.append(s+a)
            return now_res           
        for d in digits:
            res = reduce(res,alphas[d]) 
        return res 
      
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0 :
            return []
        alphas = { 2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],
        5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],
        9:["w","x","y","z"]}
        answer :List[str]= []
        stack :List[str,int]= [["",0]] 
        while stack :
            now_str,index= stack.pop()
            if index == length :
                answer.append(now_str)
                continue
            for alpha in alphas[int(digits[index])]:
                stack.append([now_str+alpha,index+1])
        return sorted(answer)
