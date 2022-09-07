class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m: dict[str,List[str]] = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if m.get(sorted_str) :
                m[sorted_str].append(str)
            else :
                m[sorted_str] = [str]
        return m.values() 
    
# for loop에서 연산을 수행하는 것보단 for loop 밖에서 전처리를 미리 해주자    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys: List[str]= ["".join(sorted(str)) for str in strs]
        m: dict[str,List[str]] = {}
        for str,key in zip(strs,keys):
            if m.get(key) :
                m[key].append(str)
            else :
                m[key] = [str]
        return m.values() 
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        [m[tuple(tuple(sorted(str)))].append(str) 
            for str in strs]
        return m.values()
