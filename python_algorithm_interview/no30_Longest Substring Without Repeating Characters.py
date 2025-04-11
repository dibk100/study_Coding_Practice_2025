'''
🍪문제 번호 :
ch11_Hash Table
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

🍊풀이 시간 :
10m

🍒풀이 방법 :
index()함수 활용하면 그리디하게 금방 풀 수 있긴함. 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = ''
        result = 0
        for ch in s :
            if ch not in tmp :
                tmp +=ch
                result = max(result,len(tmp))
            else :
                i = tmp.index(ch)
                tmp = tmp[i+1:] + ch
                result = max(result,len(tmp))
        
        return result
            
