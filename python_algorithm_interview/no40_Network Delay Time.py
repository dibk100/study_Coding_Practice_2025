'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/network-delay-time/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
bfs문제로 확인됨. 그래서 39번 풀이를 수정해봤지만 에러가 떠서 해결하지 못함. 로직은 맞는 거 같은데 자꾸 integer에러가 뜸.
solution 암기하기.

'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList={i:[] for i in range(1, n+1)}           # 노드 딕셔너리
        for dep, arrival, time in times:
            adjList[dep].append((arrival, time))
            
        q=[k]                                       # k노드부터 시작
        costs=[float("inf")]*(n+1)                  # n 노드수 설정, 양의 무한대 설정
        costs[0]=costs[k]=0                         # 0번 노드는 원래 값이 0이고, k노드도 시작 노드기 때문에 0
        
        while q:
            departure=q.pop(0)
            
            for arrival, time in adjList[departure]:
                
                if costs[departure]+time <costs[arrival]:       # 의미 : 도착지의 값이 무한값 -> 아직 방문하지 않은 노드
                    costs[arrival]=costs[departure]+time        # 그래서 해당 cost를 재설정하고 순회할 노드로 q에 추가
                    q.append(arrival)
        return -1 if any([cost==float("inf") for cost in costs]) else max(costs)        # 하나라도 무한 값이 있으면 순회하지 못한 것 == example3같은 상황. 그러면 -1 아니라면 costs에서 가장 많은 값

# falied
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u,v,w in times :
            graph[u].append([v,w])

        def bfs(start_node):
            if start_node not in graph : 
                return 0

            count = 0
            for v,w in graph[start_node] :
                count = max(count,w)
                count += bfs(v)

            return count
        
        result = bfs(k)
        return result