'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/insertion-sort-list/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
오랜만에 링크드리스트 구현하려니 머리 CPU가 느려진다. swap을 잘 활용해야함.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = root = ListNode(None)

        while head :
            cur, _ = head, head.next
            cur.next = None

            while nodes.next and nodes.next.val < cur.val :
                nodes = nodes.next
            
            nodes.next, cur.next = cur, nodes.next

            head = _
            nodes = root
        
        return root.next