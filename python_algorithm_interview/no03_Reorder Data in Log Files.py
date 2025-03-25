'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/reorder-data-in-log-files/description/

🍊풀이 시간 :
문제 이해 7분
문제 풀이 10분

🍒풀이 방법 :
sort에 lambda 사용하는 방법 다시 배움.
for logs : O(n)
split()[1] : O(1)
sort() : len(s) log len(s) -> NlogN


데이터에 따른 시간 복잡도
N < 500 : O(n^3)
N < 2,000 : O(n^2)
N < 100,000(10^4) : O(NlogN)
N < 10,000,000 (10^6) : O(N)

'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []

        for log in logs :
            if log.split()[1].isdigit():
                digit.append(log)
            
            else :
                letter.append(log)
        
        letter.sort(key = lambda x : (x.split()[1:],x.split()[0]))

        return letter+digit