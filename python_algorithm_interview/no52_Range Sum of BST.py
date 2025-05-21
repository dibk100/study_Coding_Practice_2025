'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/range-sum-of-bst/description/

🍊풀이 시간 :
20m

🍒풀이 방법 :
이 문제가 이렇게 오래 걸리 문제였을까. 제약조건을 잘못 설정해서 헤맸다.

'''
class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if not node : return

            if node.val >= low and node.val <=high :
                self.result += node.val

            if node.left :
                dfs(node.left)
            if node.right :
                dfs(node.right)

            return
        
        dfs(root)
        return self.result