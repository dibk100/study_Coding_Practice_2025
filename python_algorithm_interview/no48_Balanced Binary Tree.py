'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/balanced-binary-tree/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
풀 수 있었을 것 같은데 아쉽다. 다시 풀어보면 좋을 것 같음

'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def function(root):
            if not root : return 0

            left = function(root.left)
            right = function(root.right)

            if abs(left-right)>1 :
                return -1
            elif left==-1 or right==-1 :
                return -1
            else :
                return max(left,right)+1
    
        return function(root)!=-1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node : return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 :
                return False

            return left + 1
        
        ans = dfs(root)

        return True if ans else False