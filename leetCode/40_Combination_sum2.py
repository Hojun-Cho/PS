class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer: List[List[int]] = []
        candidates.sort()
        length = len(candidates)
        def perm(now_arr: List[int],index,now_sum: int):
            for i in range(index,length) :
                # 정렬된 리스트로 조합을 만든다, [1,1,1,1,1,1,...] 이런 경우에 중복을 제거하지 않으면 시간초과, 즉 14라인의 if문은 없어도 작동하지만 중복 제거가 필요
                if i > index and candidates[i] == candidates[i-1] : 
                    continue 
                # 합이 작은 경우에만 재귀를 수행한다.
                if now_sum + candidates[i] == target :
                    answer.append(now_arr + [candidates[i]])
                elif now_sum + candidates[i] < target :
                    perm(now_arr + [candidates[i]],i+1, now_sum + candidates[i])  
        perm([],0,0)
        return answer  
