'''
🍪문제 번호 :
ch18_binary_search
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
max함수를 사용하고 싶지만 시간복잡도가 O(N)임.
힌트가 k의 위치를 찾는 것 같음 -> pivot을 찾고
mid_pivot을 구현해서 나중에 따로 인덱스 계산하지 않아도 됨. 이건 편하네. 암기하기

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums : return -1

        # 투포인터
        left,right = 0, len(nums)-1
        while left < right :
            mid = left + (right-left)//2

            if nums[mid] > nums[right]:
                left = mid +1
            else :
                right = mid
        
        pivot = left
        start,end = 0, len(nums)-1
        while start < end :
            mid = start + (end-start)//2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] == target :
                return mid_pivot
            elif nums[mid_pivot] < target :
                start = mid +1
            else :
                end = mid
        
        return -1
