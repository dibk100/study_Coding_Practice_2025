'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/minimum-height-trees/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
양방향 그래프, 원래는 deque()를 활용해야함.
마지막에는 결국 2개 노드만 남고, 그래프의 key-val이 일대일로 하나만 남았을때 트리거로 넘겨줘야함.
트리 문제 너무 재미없는데 풀어야겠지ㅠ

'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = {i:[] for i in range(n+1)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:          # 리프가 하나 이상인 경우 중간 노드.
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:       # 트리거 역할, 해당 노드의 리프가 1개만 남아서 우리가 원하는 정답노드임을 여기서 걸름.
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

