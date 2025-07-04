'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/sort-colors/

🍊풀이 시간 :
failed

🍒풀이 방법 :
너무 어렵게 생각했던 것 같음. 정렬 문제가 나오면 O(N)으로 풀어볼 생각을 할 것.

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b = 0,0,0,

        for num in nums :
            if num == 0 :
                r+=1
            elif num ==1:
                w+=1
            else :
                b +=1

        for i in range(0,r):
            nums[i] = 0
        
        for i in range(r, r+w):
            nums[i] = 1
        
        for i in range(r+w,r+w+b):
            nums[i] = 2
