'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/invert-binary-tree/description/

🍊풀이 시간 :
3m

🍒풀이 방법 :

'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root : return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right =left

        return root