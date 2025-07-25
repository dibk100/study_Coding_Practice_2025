'''
🍪문제 번호 :
ch21
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

🍊풀이 시간 :


🍒풀이 방법 :
흐름. 리스트에서 가장 작은 값 찾기(인덱스) - 그 인덱스 기준으로 가장 큰 값 찾아가기?
방법. 투 포인터 사용하기
주의. prices리스트가 복잡하게 구성되어 있으면 투포인터 알고리즘이 복잡함. 한칸 비교만 가능한 알고리즘으로 구현함.
궁금. prices에 중복 값이 있나?

풀기는 했는데 코드가 너무 구리다. 문제에 조건이 많지 않아서 한 칸 비교만 할거면 투포인터로 구현하지 않아도 괜찮았을 거 같음

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1 : return 0
        profit = 0
        p1,p2 = 0,1

        while p1<p2 and p2 < len(prices) :
            if prices[p1] < prices[p2] :
                for p3 in range(p2, len(prices)-1):
                    if prices[p3] > prices[p3+1] :
                        profit += prices[p3] - prices[p1]
                        p2 = p3
                        break
                else :
                    p2 = len(prices)-1
                    profit += prices[p2] - prices[p1]
            
            p1 = p2
            p2 = p2+1
        
        return profit
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit