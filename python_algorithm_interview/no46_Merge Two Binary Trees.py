'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/merge-two-binary-trees/

🍊풀이 시간 :
3m

🍒풀이 방법 :
45번 풀이와 비슷하게 풀이함.

'''
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2 : return root1 if root1 else root2

        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)

        root1.val +=root2.val

        return root1