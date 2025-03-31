'''
🍪문제 번호 :
ch07_Array
https://leetcode.com/problems/array-partition/description/

🍊풀이 시간 :
3m

🍒풀이 방법 :
제약 조건인 1 <= n <= 10^4를 확인하고 sort함수 사용할 수 있겠다고 판단함.
(수정사항)어차피 정렬했다면 홀수번째가 min값이라 min함수를 사용하지 않아도 되었음.

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        # for i in range(len(nums))[::2] :
        #     result += min(nums[i],nums[i+1])
        for i in range(1,len(nums),2):
            result +=nums[i]
        
        return result