'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
dfs풀이로 노드를 훝는 건 알겠는데 root를 다시 구성하는 게 아직 어렵다.
result와 root.val을 swap하는게 킥인 거 같음. 이 구성을 암기하기

'''
class Solution:
    result = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root :
            self.bstToGst(root.right)
            self.result +=root.val
            root.val = self.result
            self.bstToGst(root.left)
        
        return root
    
# failed
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,curr):
            if not node.right : return node

            right = dfs(node.right,curr)
            curr_ = node.val+right.val + curr

            if node.left :
                dfs(node.left,curr_)
            
            return curr_
