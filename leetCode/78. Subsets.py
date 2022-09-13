class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]] 
        self.combi(nums,[],answer,0,len(nums))
        return answer 
    def combi(self,nums: List[int],curr: List[int],answer: List[int], n: int,length: int):
        for i in range(n,length):
            answer.append(curr + [nums[i]])
            if i < length-1 :
                self.combi(nums,answer[-1],answer,i+1,length)
            
            
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            # [] +[2] = [2] 
            temp = [last + [num] for last in result] 
            result += temp
        return result
            
            
            
        
        
            
            
        
        
            
