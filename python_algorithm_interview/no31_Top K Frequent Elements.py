'''
🍪문제 번호 :
ch11_Hash Table
https://leetcode.com/problems/top-k-frequent-elements/description/

🍊풀이 시간 :
10m

🍒풀이 방법 :
counter라이브러리 활용

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x,y in Counter(nums).most_common(k)]