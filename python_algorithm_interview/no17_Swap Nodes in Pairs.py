'''
🍪문제 번호 :
ch08_Linked_list 
https://leetcode.com/problems/swap-nodes-in-pairs/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
머리에 들어오지 않음.. 다시 풀기..

'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head

        pointer = output = ListNode()
        
        while head and head.next :
            prve,after = None,None
            
            after, _, head.next = head.next, head.next.next, prve
            prve =  head
            after.next =  prve
            head = _

            pointer.next = after
            pointer = pointer.next.next

        pointer.next = head if head else None
        
        return output.next