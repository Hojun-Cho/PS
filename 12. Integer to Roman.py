# 처음 풀이 : 제일 작은 단위부터 나눠간다.
class Solution:
    def intToRoman(self, num: int) -> str:
        symbols : dict[int,str] = {
            1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",
            4 :"IV", 9 :"IX",
             40:"XL" , 90:"XC",
             400 : "CD" , 900:"CM"
        }
        answer = [] 
        curr = 1
        while num != 0 :
            mod =  num % 10
            mod *= curr 
            temp = [] 
            while mod > 0 :
                if symbols.get(mod):
                    temp.append(symbols[mod])
                    mod -= mod 
                else :
                    x = symbols.get(curr)
                    mod -= curr 
                    temp.append(x)
            answer.append("".join(temp[::-1]))
            curr *= 10
            num = num // 10 
        return "".join(answer[::-1])
      
# 가장 큰 로마 숫자부터 확인한다
# 만약 가장 큰 로마 숫자로 나눠지지 않는다면 이는 그 자릿수가 로마 숫자보다 작다는 의미이고, 따라서 더 작은 로마 숫자로 이동한다
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000] ]   

        answer =""
        for sym,val in roman[::-1]:
            if num // val :
                count = num // val 
                answer += sym * count 
                # num = 723, val = 500 => num = 223 
                num = num % val 
        return answer
