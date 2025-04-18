'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/combinations/description/

🍊풀이 시간 :
20m

🍒풀이 방법 :
로직은 5분만에 만들었는데 result에 값을 저장하는데 자꾸 문제가 생겼었음. [:]로 해결 완료

'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i+1 for i in range(n)]
        result = []

        def dfs(idx,tmp):
            if len(tmp)==k:
                result.append(tmp[:])           # result.append(tmp)로 했는데 result의 값이 tmp와 연동되어서 자꾸 문제가 생겼었음.
                return
            
            for i in range(idx,n):
                tmp += numbers[i],
                dfs(i+1,tmp)
                tmp.pop()
            
            return
        dfs(0,[])
        return result