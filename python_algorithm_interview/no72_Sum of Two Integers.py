'''
🍪문제 번호 :
ch19_bit
https://leetcode.com/problems/sum-of-two-integers/description/

🍊풀이 시간 :


🍒풀이 방법 :
모르겠다 암기.. 이진수(자릿수)와 xor개념에 대해 다시 공부 필요

'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff                               # 32개의 1로 이뤄진 2진수 = 11111111111111111111111111111111 (2진수)
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a&mask if b > mask else a    

