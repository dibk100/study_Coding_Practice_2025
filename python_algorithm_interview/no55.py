'''
🍪문제 번호 :
ch15_heap
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

🍊풀이 시간 :
failed(10m) - time limit exceeded

🍒풀이 방법 :
힙 모듈을 쓰지 않고 풀려고 했더니 정렬로 풀어버렸음. 저렇게 풀거면 sort()하고 nums[-k]를 하지.. 내 풀이 진짜 바보 같다.
힙 모듈 사용하는게 빠름. 특히 heapq.nlargest(k,nums)[-1]하면 한 줄에 완료
다른 풀이 봤는데 pivot 풀이가 순위가 높았음. 정렬 풀이식 같은데 일단 이해 못해서 패스

'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
# failed 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        orders = [None]*len(nums)

        for c in nums :
            for i in range(len(orders)):
                if orders[i]== None : 
                    orders[i] = c
                    break
                elif c < orders[i] :
                    orders[i],c = c,orders[i]
        
        return orders[-k]