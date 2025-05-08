'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/diameter-of-binary-tree/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
42번 풀이처럼 풀다가 실패.
뎁스 끝의 노드를 -1로 설정해서 result(length)와 비교하는 작업으로 노드와 엣지 차이를 둬서 계산한 것이 핵심 같음.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    length = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node : return -1

            # 각 노드의 뎁스 끝까지 확인
            left = dfs(node.left)
            right = dfs(node.right)

            self.length = max(self.length,left+right+2)     # 뎁스 끝에서 (-1)+(-1)+2 = 0

            return max(left,right) +1                       # 결국 해당 노드는 left, right값 중 엣지 하나를 갖고 상위 노드로 회귀

        dfs(root)
        return self.length
        