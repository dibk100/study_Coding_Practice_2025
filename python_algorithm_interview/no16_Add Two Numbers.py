'''
🍪문제 번호 :
ch08_Linked_list 
https://leetcode.com/problems/add-two-numbers/description/

🍊풀이 시간 :
30m

🍒풀이 방법 :
Linked list 자체에 대한 이해가 부족한 것이 느껴지는 문제.
지금 풀이보다 더 효율적인 풀이를 고민해봐야 할 것 같음. int -> str -> int 과정이 비효율적으로 보임.

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ''
        l2_str = ''

        while l1 :
            l1_str += str(l1.val)
            l1 = l1.next
        
        while l2 :
            l2_str += str(l2.val)
            l2 = l2.next

        result = str(int(l1_str[::-1]) + int(l2_str[::-1]))

        move = output = ListNode()                                      # 이 부분에서 수정이 많았음.
        for i in result[::-1] :
            move.next = ListNode(int(i))
            move = move.next

        return output.next