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
      
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        [m[tuple(tuple(sorted(str)))].append(str) 
            for str in strs]
        return m.values()
