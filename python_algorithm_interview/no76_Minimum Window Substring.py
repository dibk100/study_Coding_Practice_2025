'''
🍪문제 번호 :
ch20_sliding window
https://leetcode.com/problems/minimum-window-substring/

🍊풀이 시간 :


🍒풀이 방법 :
알파벳 존재하는지 확인 - 윈도우 안에서 줄일 수 있는지 확인 - 다음 루프
for 문 안에 while문 구조

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]