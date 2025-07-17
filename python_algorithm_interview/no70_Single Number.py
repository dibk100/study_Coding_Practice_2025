'''
🍪문제 번호 :
ch19_bit
https://leetcode.com/problems/single-number/description/

🍊풀이 시간 :


🍒풀이 방법 :
19장 비트조작 파트는 거의 암기해야할 것 같음.
기억해두면 나중에 잘 쓰일 것 같음

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num   
            print(result)        

        return result