'''
🍪문제 번호 :
ch08_Linked_list 
https://leetcode.com/problems/merge-two-sorted-lists/description/

🍊풀이 시간 :
30m

🍒풀이 방법 :
30분이나 걸리는 문제는 아닌 것 같음.
linked list 형태를 제대로 이해하지 못해서 초반에 구조이해에 시간을 소요함.
현재 코드도 너무 길고 반복이 많아서 마음에 들지 않음..

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2 : return list2 if not list1 else list1
        nodes= move = ListNode

        while list1 and list2 :
            if list1.val == list2.val :
                move.next, list1 = list1,list1.next
                move.next.next, list2 = list2, list2.next
                move = move.next.next
            
            elif list1.val < list2.val :
                move.next, list1 = list1, list1.next
                move = move.next
            else :
                move.next, list2 = list2, list2.next
                move = move.next
        
        if list1 :
            move.next, list1 = list1, list1.next
        elif list2 :
            move.next, list2 = list2, list2.next

        return nodes.next
    
# 수정본
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2 : return list2 if not list1 else list1
        nodes= move = ListNode

        while list1 and list2 :
            # 수정
            if list1.val <= list2.val :
                move.next, list1 = list1, list1.next
            else :
                move.next, list2 = list2, list2.next
            
            move = move.next
        
        # 수정
        move.next = list1 if list1 else list2

        return nodes.next
