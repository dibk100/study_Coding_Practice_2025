'''
🍪문제 번호 :
ch07_Array
https://leetcode.com/problems/3sum/description/

🍊풀이 시간 :


🍒풀이 방법 :
데이터에 따른 시간 복잡도
N < 500 : O(n^3)
N < 2,000 : O(n^2)

데이터는 3000개라서 3중 for문 실패 >> 이중 for문에서 끝내기 or two pointer?

'''

# failed
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        save = []
        for p1 in range(len(nums)-3):
            for p2 in range(p1+1,len(nums)-2) :
                for p3 in range(p2+1,len(nums)-1) : 
                    if nums[p1] + nums[p2] + nums[p3] ==0 :
                        save.append([nums[p1],nums[p2],nums[p3]])
        return save