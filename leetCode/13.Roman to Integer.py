class Solution:
    def romanToInt(self, s: str) -> int:
        symbols: dict[str,int] = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
                                 "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        answer = 0
        i = 0
        while i < len(s) :
            if symbols.get(s[i:i+2]) :
                answer += symbols[s[i:i+2]]
                i+=2
            else :
                answer += symbols[s[i]]
                i+=1 
        return answer 
    
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols: dict[str,int] = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        answer = 0
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        for symbol in s :
            answer += symbols[symbol]
        return answer 
