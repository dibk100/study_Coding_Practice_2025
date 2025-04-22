'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/combination-sum/description/

🍊풀이 시간 :
18m

🍒풀이 방법 :
재귀로 풀어야겠다고 직관적으로 생각함. [2,2,3]에서 같은 위치였던 2를 확인하러 가는 플로우라서 딥하게 재귀한다고 생각한 것 같음.

'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        output = []
        def dfs(idx,tmp):
            if sum(tmp) == target :
                output.append(tmp[:])
                return
            elif sum(tmp) > target :
                return

            for i in range(idx,size) :
                dfs(i,tmp+[candidates[i]])
            return

        candidates.sort()
        dfs(0,[])

        return output        