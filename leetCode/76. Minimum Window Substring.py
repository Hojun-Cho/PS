class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # missing : removed target count 
        need,missing = Counter(t),len(t)
        i=0
        start,end = 0,sys.maxsize
        # j는 현재 위치 
        for j,c in enumerate(s,1):
            # 만약 need[c] > 0 이면 이는 Target이라는 의미이다 , 따라서 missing을 -1
            if need[c] > 0 :
                missing-=1 
            # Target에 존재하지 않는 값이면 need[c] 는 항상 < 0 이다.
            # need[c] <0 의 의미는 Target에 포함되지 않는 값이라는 의미 
            need[c] -= 1 
            # 포함된 범위를 처음 찾은경우 or 이미 찾은 경우 새로운 범위를 탐색 
            if not missing :
                while i < j and need[s[i]] < 0 :
                    need[s[i]] +=1 
                    i+=1
                if end-start > j- i :
                    start,end = i,j
        return s[start:end] if end != sys.maxsize else ""
                    
