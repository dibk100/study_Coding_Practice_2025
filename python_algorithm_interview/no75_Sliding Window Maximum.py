'''
🍪문제 번호 :
ch20_sliding window
https://leetcode.com/problems/sliding-window-maximum/

🍊풀이 시간 :


🍒풀이 방법 :
deque를 사용하지 않고 풀려고 했는데 실패함. que 특징이 pop하면 맨 뒤 요소가 제거됨. popleft기능이 있음.
그리고 풀이를 살펴보니, nums의 값이 아닌 인덱스 값을 저장함.
모르겠다. 알것같다가 모르겠다 나중에 다시 풀어야할 것 같음


'''

# 너무 그리디하게 풀었음. 윈도우 사이즈를 고려하지 못함. 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        for i in range(k) :
            if not result :
                result += nums[i],
            elif result and result[-1] < nums[i] :
                result[-1] += nums[i],
        
        for j in range(k,len(nums)) :
            print(nums[j])
            if result[-1] < nums[j] :
                result += nums[j],
            else :
                result += result[-1],
        
        return result

# 너무 쉽게 생각했나, Time Limit Exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(nums)-k+1) :
            result +=max(nums[i:i+k]),
        
        return result