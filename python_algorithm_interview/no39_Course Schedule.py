'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/course-schedule/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
참고 https://engineercoding.tistory.com/171

나는 딕셔너리 형태로 진행하려고 함. dfs함수에서 for문을 돌릴때 딕셔너리는 값이 없으면 오류가 뜸! 이거 주의하기

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites :
            graph[a].append(b)

        visited = [0] *numCourses

        def dfs(node):
            if visited[node]==1 :return False           ## 순환구조
            if visited[node]==2 : return True           ##

            visited[node] = 1                           # 순환 구조 확인하기 위한 트릭
            for n in graph[node]:
                if not dfs(n) :                         # return 값이 False라는 건 순환
                    return False
            visited[node] = 2                           # 무사히 마치면 2로 방문했다는 기록
            return True
        
        for i in range(numCourses):
            if visited[i]==0 and not dfs(i):
                return False
        
        return True