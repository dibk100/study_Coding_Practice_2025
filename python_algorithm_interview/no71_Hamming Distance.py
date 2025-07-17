'''
🍪문제 번호 :
ch19_bit
https://leetcode.com/problems/hamming-distance/description/

🍊풀이 시간 :


🍒풀이 방법 :
비트 연산자 공부

'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

