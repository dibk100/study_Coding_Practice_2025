'''
🍪문제 번호 :
ch12_graph
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

🍊풀이 시간 :
40m

🍒풀이 방법 :
겨우겨우 풀음.
재귀 함수의 경우 재귀로 들어가기 전에 트리거(ex if문)으로 멈추는 제약조건을 꼭 입력해야 무한재귀가 되지 않음.

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alnum_table = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) <=1 : return alnum_table[digits] if digits else []
        
        out = []
        def dfs(num,idx,in_tmp):
            if idx == len(digits) :
                for al in alnum_table[num] :
                    tmp = in_tmp + al
                    out.append(tmp)
                return

            for al in alnum_table[num] :
                tmp = in_tmp + al
                dfs(digits[idx],idx+1,tmp)

            return

        dfs(digits[0],1,'')
        return out

# 이전 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : return []
        
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []

        def recursive_dfs(idx,path):
            if len(path) == len(digits) :
                ans.append(path)
                return

            for i in range(idx, len(digits)) :
                for j in phone[digits[i]] :
                    recursive_dfs(i+1,path+j)
            return

        recursive_dfs(0,'')
        return ans