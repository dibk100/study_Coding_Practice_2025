'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
bfs인지 dfs인지 감을 잡지 못함. 결국 dfs로 풀어보려고 했지만 실패. 답지를 확인해보니 bfs문제여서 재귀풀이로 해결 불가능한 문제였음. 40번과 비슷한 풀이..
solution 암기하기.

'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjTable = {i:[] for i in range(n+1)}
        for dep,arr,price in flights :
            adjTable[dep].append([arr,price])
        
        q = [(src,0,0)]                 # 출발지, 누적가격, 뎁스
        costs=[float('inf')]*n
        
        while q:
            departure,cum_price,depth = q.pop(0)
   
            if depth <= k : 
                for arrival, price in adjTable[departure] :
                    cost = cum_price + price
                    if costs[arrival] > cost :
                        costs[arrival] = cost
                        q.append((arrival,cost,depth+1))
        
        return -1 if costs[dst]==float('inf') else costs[dst]

# failed
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for f,t,p in flights :
            graph[f].append([t,p])
        
        def dfs(f,t,count,result):
            if count < 0 : return 0 

            for next_,price in graph[f] :
                result +=price

                if count == 0 and next_==t : return result

                boo_ = dfs(next_,t,count-1, result)
                if boo_ == 0 : return 0
                result +=boo_
    

            print('ddd',result)
            return result

        result = dfs(src,dst,k,0)
        return result
        