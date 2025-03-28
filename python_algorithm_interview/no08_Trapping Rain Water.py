'''
🍪문제 번호 :
ch07_Array
https://leetcode.com/problems/trapping-rain-water/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
# failed : max(), index() 함수 -> O(N) 시간 복잡도 --> N^2 주의
# 15분 풀이 고안 : merge sort함수 활용하기 > 양 끝에 확인하는 작업을 못함..

'''

class Soultion :
    def merge_sort(self,arr: List[int]) -> int :
        
        if len(arr) <= 2 :
            return 1
        
        mid = arr.index(max(arr))
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid+1:])
        
        return right + left
    
    def trap(self, height: List[int]) -> int:
        output = self.merge_sort(height)
        
        return output

class Solution:
    def merge_sort(self,arr: List[int]) -> int :
        if len(arr) <= 1 :
            return 1

        mid = arr.index(max(arr))
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid+1:])

        print(right + left)
        return right + left
    
    def trap(self, height: List[int]) -> int:
        output = self.merge_sort(height)
        
        return output
    
### solution
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0

        volume = 0
        left,right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left<right :
            left_max, right_max = max(height[left],left_max), max(height[right],right_max)

            if left_max <= right_max :
                volume += left_max - height[left]
                left +=1
            else :
                volume += right_max - height[right]
                right -=1

        return volume