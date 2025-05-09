'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/longest-univalue-path/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
bfs라고 생각했는데 다른 풀이를 보니 dfs로 풀었다.. bfs로 풀 수 있을 것 같은데 아직 이 풀이로 해결하지 못함.
dfs 풀이도 반복이 많고 recursive를 제대로 활용하지 못하는 풀이 같아서 마음에 들지 않음.
다른 solution 내용을 뜯어보니, dfs에 (curr_node, parent_root) 두 개의 파라미터 비교하며 작업을 함. 다른문제에도 이런 풀이를 활용하게 될 것 같음.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node) :
            if node is None : return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val :
                left +=1
            else :
                left = 0
            if node.right and node.val == node.right.val :
                right +=1
            else :
                right = 0
            
            self.result = max(self.result, left+right)
            
            return max(left,right)
        
        dfs(root)
        return self.result

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        q = [(root,0)]
        result = 0

        while q :
            node, sum_accum = q.pop()
            result = max(sum_accum,result)
            print(node.val, result)

            if node.right and node.val == node.right.val :
                q.append((node.right,sum_accum+1))
            if node.left and node.val == node.left.val :
                q.append((node.left,sum_accum+1))  

            if not (node.right and node.val == node.right.val) and not (node.left and node.val == node.left.val) :
                if node.right :
                    q.append((node.right,sum_accum))
                if node.left : 
                    q.append((node.left,sum_accum))

        return result
        