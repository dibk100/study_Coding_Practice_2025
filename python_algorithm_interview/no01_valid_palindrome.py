'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/valid-palindrome/description/

🍊풀이 시간 :
10m

🍒풀이 방법 :
two-pointer 기법으로 문자열의 양 끝에서 확인하는 작업을 함. -> O(n/2) = O(n)
세팅부분에서 for문을 통해 문자열 검사, lower함수를 사용함. -> O(n), 공간 복잡도
최종적으로 O(n)

'''

class Solution :
    def isPalindrome(self,s:str) -> bool :
        res = [i for i in s.lower() if i.isalnum()]     # i.isalpha() > i.isalnum()
        left, right = 0, len(res)-1
        
        while left < right :
            if res[left] != res[right] :
                return False
            left+=1
            right-=1
            
        return True

# other solution
class Solution :
    def isPalindrome(self,s:str) -> bool :
        res = ''.join(filter(str.isalnum,s)).lower()
        return res==res[::-1]