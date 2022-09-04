from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer: List[List[int]] = [] 
        candidates.sort()
        length = len(candidates)
        def dfs(remain,index: int, stack: List[int])-> None:
            if remain == 0 :
                answer.append(stack)
            for i in range(index,length):
                if candidates[i] > remain :
                    return 
                dfs(remain - candidates[i],i,stack + [candidates[i]])
        dfs(target,0,[])
        return answer 
