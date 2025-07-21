'''
🍪문제 번호 :
ch19_bit
https://leetcode.com/problems/number-of-1-bits/description/

🍊풀이 시간 :


🍒풀이 방법 :
71번 문제 다운그레이드 버전인가?

'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')