from typing import List
# 1 
class Solution:
		# time out => [5,4,3,2,1] 내림차순 정렬인 경우에 발생한다 O(n^2)
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0 
        buy_index = 0 
        for i,buy in enumerate(prices):
            if buy > prices[buy_index] :
                continue 
            for j in range(i,len(prices)):
                if max_price <= prices[j] - buy  :
                    max_price = max(max_price, prices[j]-buy)
                    buy_index = j 
                
        return max_price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0 
        min_price = sys.maxsize
        
        for price in prices :
            # 가장 최솟값을 구한다
            min_price = min(min_price,price)
            answer = max(answer,price - min_price)
        return answer
# 2 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = prices[0] 
        # 팔고 같은 day에 다시 산다. 5에서 사고 3에서 팔고 3에서 다시 산다.
        # 팔 수 있는경우 무조건 판다
        for price in prices :
            if price > buy :
                answer += (price-buy)
            buy = price 
        return answer 
