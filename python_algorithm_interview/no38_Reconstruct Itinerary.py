'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/reconstruct-itinerary/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
참고 https://velog.io/@kkuoo7/Leetcode-332.-Reconstruct-Itinerary

'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        for fi,ti in sorted(tickets):
            flights[fi] = flights.get(fi,[]) + [ti]
        for k,v in flights.items():
            flights[k].sort()

        route = []
        def dfs(departure): 
            if departure not in flights :
                route.append(departure)
                return

            while flights[departure]:  
                dfs(flights[departure].pop(0))
            route.append(departure)
          
        dfs('JFK')
        
        return route[::-1]          ## dfs에서 가장 딥한 뎁스, 도착지부터 입력되기 때문에 역순으로 출력해야함