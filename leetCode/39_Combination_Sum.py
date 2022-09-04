from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer: List[List[int]] = [] 
        candidates.sort()
        length = len(candidates)
        def perm(index,sum: int,arr: List[int]) -> None:
            for i in range(index,length):
                if sum + candidates[i] > target : 
                    return 
                elif sum + candidates[i]  == target :
                    answer.append(arr+[candidates[i]])
                    return 
                else :
                    if index == i :
                        perm(index, sum+candidates[i] , arr+ [candidates[i]])
                    else :
                        perm(i, sum+candidates[i] , arr+ [candidates[i]])

        perm(0,0,[])
        return answer 
