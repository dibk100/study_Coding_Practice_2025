'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

🍊풀이 시간 :
25m

🍒풀이 방법 :
시간복잡도를 고려해서 수정함. deque를 사용하면 n제곱에서 nlogn으로 줄일 수 있음.
다른 솔루션도 봤는데, dsf방식으로 풀어 낸 풀이도 신박함. 시간 복잡도, 공간 효율성 부분에서 효율적 - 이 코드 암기하기

'''
from collections import deque
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []
        q = deque([root])

        while q :
            node = q.popleft()          # O(n)

            if node :
                nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
        nodes.sort()                # nlogn

        result = float('inf')           # float inf 이 함수 잘 활용해보기

        for i in range(1,len(nodes)):
            result = min(nodes[i]-nodes[i-1],result)
        
        return result
    
    
# other solution
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, min_diff = None, float('inf')

        def dfs(node):
            if not node:
                return

            dfs(node.left)                              # 1. 입력 노드 기준 왼쪽 끝까지 확인 후,

            nonlocal prev, min_diff

            if prev:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node                                         # 2. prev에 왼쪽 끝까지 간 노드으로 선언

            dfs(node.right)                                     # 3. 그 노드의 오른쪽을 다시 루프(1번으로)

        dfs(root)
        return min_diff