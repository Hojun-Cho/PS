class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = [] 
        for n in nums:
            if n in answer :
                answer.remove(n)
            else :
                answer.append(n)
        return answer[0]
