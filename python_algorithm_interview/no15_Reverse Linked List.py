'''
🍪문제 번호 :
ch08_Linked_list 
https://leetcode.com/problems/reverse-linked-list/description/

🍊풀이 시간 :
7m

🍒풀이 방법 :
no13의 문제 풀이를 활용함.
no13보다 이 문제를 먼저 풀었으면 그 문제가 더 쉬웠을 거 같은데..

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = None
        while head :
            nodes,nodes.next,head = head, nodes,head.next
        return nodes