'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

🍊풀이 시간 :
4m

🍒풀이 방법 :
dfs풀이로 뎁스 가장 밑까지 확인 후 리턴하는 방식으로 계산함.
하지만 풀이를 확인을 해보니 bfs로 풀이 가능함.
나는 dfs풀이가 너무 익숙해서 bfs, stack으로 풀어내는 풀이가 낯설게 느낌. bfs풀이를 잘 구현하도록 노력하기

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node : return 1

            a = dfs(node.left)
            b = dfs(node.right)

            return max(a,b)+1
        
        result = dfs(root)

        return result-1
    

# other solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 1
        stack = [(root,1)]
        max_level = 0

        while stack:
            node, level = stack.pop()
            max_level = max(level, max_level)

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return max_level