'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/number-of-islands/

🍊풀이 시간 :
14m

🍒풀이 방법 :
dfs방식으로 방문 노드를 기록하며 순회함.
다른풀이를 참고하면, 나처럼 visited를 생성하지 않고 grid에 방문 표기(0)를 하며 순회함.

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        def dfs(row,col):

            for x,y in direction :
                mx = row+x
                my = col+y

                if mx < 0 or mx >= len(grid) or my < 0 or my >= len(grid[0]):
                    continue

                if grid[mx][my] == '1' and visited[mx][my] == False :
                    visited[mx][my] = True
                    dfs(mx,my)

            return 1

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j]=='1':
                    count +=dfs(i,j)

        return count

        