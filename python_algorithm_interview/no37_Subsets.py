'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/subsets/description/

🍊풀이 시간 :
4m

🍒풀이 방법 :
나에게 위의 조합, 순열 문제보다 더 직관적으로 이해되서 금방 풀음.

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def dfs(idx,tmp):
            if idx == len(nums):
                return

            for i in range(idx,len(nums)):
                tmp += nums[i],
                dfs(i+1,tmp)
                result.append(tmp[:])
                tmp.pop()
            return
        dfs(0,[])
        return result