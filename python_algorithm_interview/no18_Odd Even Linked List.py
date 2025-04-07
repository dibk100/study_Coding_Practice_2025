'''
🍪문제 번호 :
ch08_Linked_list 
https://leetcode.com/problems/odd-even-linked-list/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
reverse와 그냥 노드 연결하는 방법을 헷갈려해서 풀이가 자꾸 꼬임. 15번 문제도 잘 기억해두기

'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 29~
        even = e = ListNode()
        odd = o = ListNode()

        while head and head.next :
            odd.next,even.next = head, head.next
            odd, even = odd.next, even.next
            head = head.next.next
        
        if head :
            odd.next, even.next = head, None
            odd = odd.next
        
        odd.next = e.next
        return o.next