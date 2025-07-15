'''
🍪문제 번호 :
ch18_binary_search
https://leetcode.com/problems/intersection-of-two-arrays/description/

🍊풀이 시간 :
3m

🍒풀이 방법 :
이런 문제는 도데체 왜 있는거지? 문법공부?
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))