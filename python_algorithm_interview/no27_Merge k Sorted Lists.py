'''
🍪문제 번호 :
ch10_priority queue
https://leetcode.com/problems/implement-stack-using-queues/description/

🍊풀이 시간 :
10m

🍒풀이 방법 :
linked list 챕터에 해당되는 내용.
우선 각 값들을 리스트로 변환(for)
정렬 후, 새로 링크드리스트로 변환

어려운 문제가 아닌 것 같은데 문제 난이도가 높네?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []

        for l in lists :
            while l :
                tmp += l.val,
                l = l.next
        
        tmp.sort()
        t = h = ListNode()

        for c in tmp :
            t.next = ListNode(c)
            t = t.next
        
        return h.next