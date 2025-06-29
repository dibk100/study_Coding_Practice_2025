'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/largest-number/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
문자열을 10곱해서 자리수를 확인하는 방법이 키포인트.
그리고 0000 > 0으로 출력하기 위해 마지막 if문 추가 필요.

'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums.sort(key=lambda x: str(x)*10, reverse=True)
        result = ''.join(str(num) for num in nums)

        return '0' if result[0]=='0' else result