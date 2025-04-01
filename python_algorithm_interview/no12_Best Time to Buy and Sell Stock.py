'''
🍪문제 번호 :
ch07_Array
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

🍊풀이 시간 :
8m

🍒풀이 방법 :
예전에 풀었던 문제라 여러 풀이 방법이 스쳐 지나갔음.
처음에는 DP방식으로 풀려고 했는데, 직관적으로 이해하기 쉬운 구현하기 쉬운 풀이로 진행함.
내 풀이는 O(N)
other 풀이가 좀 더 효율적

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_price = 100000

        for i in range(1,len(prices)):
            if prices[i-1] < prices[i] :
                curr_price = min(curr_price,prices[i-1])
                profit = max(profit,prices[i]-curr_price)

        return profit
    
    def maxProfit_other(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        
        for price in prices :
            if price < min_price :
                min_price = price
            elif price - min_price > profit :
                profit = price - min_price
        
        return profit
