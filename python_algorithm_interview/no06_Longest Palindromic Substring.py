'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/longest-palindromic-substring/description/

🍊풀이 시간 :
failed(60m)

🍒풀이 방법 :
window size를 고정시켜서 window size를 줄여나가는 방식으로 찾으려고 함. 하지만 window가 움직이는 시작점 위치를 for문을 통해 순회해야해서 시간 복잡도 이슈, 꼬이는 이슈로 문제해결 실패

solution 풀이.
윈도우 사이즈 2, 3으로 비교하는 작업을 함.(짝수 윈도우, 홀수 윈도우)
윈도우 사이즈는 2-4-6.../3-5-7..로 커져감.

나는 윈도우 사이즈를 줄여나갈 생각을 했는데, 반대로 윈도우 사이즈를 키워가는 방법도 있었음.
ch23에서 DP풀이법도 있다고 함. 추후 다시 풀어보기

그리고 15분 안에 풀이식이 생각나지 않고, 15분 안에 구현되지 않는다면 빨리 포기하고 답지 or 다음 문제 보기..
'''
# solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lookup(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) <= 1 or s == s[::-1]: return s
        ans = ''
        for i in range(len(s)-1):
            ans = max(ans, lookup(s, i, i+1), lookup(s, i, i+2), key=len)
        return ans

# DP풀이법 참고 https://www.algodale.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, text: str) -> str:
        max_s, max_e = 0, 0
        dp = {}
        for s in range(len(text) - 1, -1, -1):
            for e in range(s, len(text)):
                if s == e:
                    dp[(s, e)] = True
                elif s + 1 == e:
                    dp[(s, e)] = text[s] == text[e]
                else:
                    dp[(s, e)] = text[s] == text[e] and dp[(s + 1, e - 1)]
                if dp[(s, e)] and max_e - max_s < e - s:
                    max_s, max_e = s, e
        return text[max_s : max_e + 1]