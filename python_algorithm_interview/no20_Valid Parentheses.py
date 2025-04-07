'''
🍪문제 번호 :
ch09_Stack and Queue
https://leetcode.com/problems/valid-parentheses/description/

🍊풀이 시간 :
8m

🍒풀이 방법 :
딕셔너리를 활용하여 순차적으로 문자를 비교확인.
후입선출 방식
'''
class Solution:
    def isValid(self, s: str) -> bool:
        test = {')':'(',"}":"{",']':'['}
        result =[]

        for ch in s :
            if ch not in test :
                result +=ch,
            else :
                if not result : return False

                c = result.pop()
                if test[ch] !=c :
                    return False
        
        return True if not result else False