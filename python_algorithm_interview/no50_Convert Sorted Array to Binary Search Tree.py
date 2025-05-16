'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

🍊풀이 시간 :
15m

🍒풀이 방법 :
1) 가운데 위치의 값을 찾아서 헤드 노드로 만들기 -> 2.함수화) 왼쪽은 왼쪽끼리, 오른쪽은 오른쪽끼리 노드만드는 방향
요즘 컨디션에 따라 문제가 빨리 풀리거나 오래걸리거나 한다. 어떤 컨디션에도 꾸준히 아웃풋이 잘 나오도록 하고 싶다.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums : return None

        idx = len(nums)//2

        node = TreeNode(nums[idx])
        node.left = self.sortedArrayToBST(nums[:idx])
        node.right = self.sortedArrayToBST(nums[idx+1:])

        return node

