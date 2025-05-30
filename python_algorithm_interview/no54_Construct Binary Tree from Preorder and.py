'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
5분 고민하고 포기한 문제. 풀이 방법을 보니 좀 더 고민했으면 풀 수도 있었을 것 같음
핵심은 preorder가 상위노드부터 리스트되어 있다는 걸 인식하고(순차적으로 노드를 뽑아낼 수 있다는 의미), inorder에서 그 노드를 찾아서 왼오로 루프를 돌아서 구현 가능함.

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder : return

        index = inorder.index(preorder.pop(0))                                      # preorder.pop(0)는 중심(상위)이 되는 node, 그 노드의 위치를 inorder에서 찾기
        node = TreeNode(inorder[index])                                             # inorder[index]로 preorder.pop(0)처럼 노드 만들기

        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])

        return node