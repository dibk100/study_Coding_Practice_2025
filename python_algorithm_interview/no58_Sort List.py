'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/sort-list/description/

🍊풀이 시간 :
5m

🍒풀이 방법 :
아 진짜 링크드 리스트 왜 자꾸 나오냐고ㅠㅠ
O(N) + O(NlogN) + O(N) = O(NlogN)   --> N<=10^5까지는 1초안에 실행됨.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head :
            nodes.append(head.val)
            head = head.next
        
        new = m = ListNode()
        nodes.sort()

        for node in nodes :
            n = ListNode(node)
            m.next = n
            m = m.next
        
        return new.next
        