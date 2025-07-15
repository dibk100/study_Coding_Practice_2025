'''
🍪문제 번호 :
ch18_binary_search
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

🍊풀이 시간 :
15m

🍒풀이 방법 :
투 포인터 방식

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2 = 0, len(numbers)-1

        while p1 < p2 :
            if numbers[p1] + numbers[p2] == target :
                return [p1+1,p2+1]
            
            elif numbers[p1] + numbers[p2] < target :
                p1 +=1
            
            else :
                p2 -=1
        
        return -1