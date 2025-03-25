'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/reverse-string/description/

🍊풀이 시간 :
7m

🍒풀이 방법 :
two-pointer기법 활용함.

'''
class Solution :
    def reverseString(self,s:List[str]) -> None :
        left, right = 0, len(s)-1
        
        while left < right :
            s[left],s[right] = s[right],s[left]
            left+=1
            right -=1
        return
