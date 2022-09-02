class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        // 답으로 나올 수 있는 최대는 최소 길이를 가진 문자열 
        short = min(strs,key = len)
        for i,ch in enumerate(short):
            for other in strs :
                if ch != other[i] :
                    return short[:i]
        return short
