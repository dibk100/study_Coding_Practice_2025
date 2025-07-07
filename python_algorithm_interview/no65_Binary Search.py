'''
🍪문제 번호 :
ch18_binary_search
https://leetcode.com/problems/binary-search/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
반성하기. 이걸 못 풀다니
while문, 양 끝에서 -1,+1하는 것 암기하기

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0, len(nums)-1

        while start <= end :
            idx = (end+start)//2

            if nums[idx] == target :
                return idx
            elif nums[idx] < target :
                start =idx+1
            else :
                end = idx-1

        return -1
