'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/permutations/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
라이브러리 사용하지 않고 풀기
recursive_dfs의 제약조건은 생각했는데, 입력변수를 인덱스와 정답담는 변수로 정했었음.
정답담는 변수, 나머지 값들 리스트 이 두개로 입렸했으면 실행되었겠구나

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursive_dfs(visited, tmp):
            if len(visited)==len(nums):
                ans.append(visited)
                return

            for i in range(len(tmp)):
                recursive_dfs(visited+[tmp[i]],tmp[:i]+tmp[i+1:])
            return
        
        for idx in range(len(nums)):
            recursive_dfs([nums[idx]],nums[:idx]+nums[idx+1:])