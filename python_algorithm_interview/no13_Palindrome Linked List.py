'''
🍪문제 번호 :
ch08_Linked_list : Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/

🍊풀이 시간 :
5m

🍒풀이 방법 :
리스트로 바꿔서 푼다면 쉬운 문제인데, 연결리스트 유지한다면 어려움
런너 기법 활용(암기하기)

'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        curr = head

        while curr :
            nodes += curr.val,
            curr = curr.next
        
        left,right = 0,len(nodes)-1
        while left <= right :
            if nodes[left] != nodes[right] :
                return False
            left +=1
            right -=1
        return True
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h = t = head
        rev_nodes = None
        
        while t and t.next :
            t = t.next.next
            rev_nodes, rev_nodes.next, h = h, rev_nodes, h.next
        
        if t :
            h = h.next
        
        while rev_nodes and rev_nodes.val == h.val:
            rev_nodes, h = rev_nodes.next, h.next
        
        return not rev_nodes