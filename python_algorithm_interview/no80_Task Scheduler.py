'''
🍪문제 번호 :
ch21
https://leetcode.com/problems/task-scheduler/description/

🍊풀이 시간 :
48~

🍒풀이 방법 :
같은 task 간에 N 간격이면 된다는 거잖아? 그러면 우선 task를 카운팅한 딕셔너리를 만들고, key에 대해 for문 돌면서 카운팅하면 되지 않나?라고 바로 생각이 듦.
N 간격 확인하는 코드가 너무 더럽게 작성됨ㅠ

솔루션 풀이 미쳤다.

n + 1 : 간격을 포함한 하나의 블록
max_freq - 1 : 블록 갯수(마지막 블록은 계산하지 않음)
+ num_max_freq : 블록 갯수에서 마지막 블록의 뒤는 계산되지 않음. 하지만 똑같이 max값과 같은 문자가 있다면 뒤에 덧붙여야함.

tasks = ["A","A","A","B","B","B"], n = 2
A _ _ | A _ _ | A
-> max_freq - 1 : 2개 블록
-> n + 1 : 3개 칸
--> 3*2 = 6
---> num_max_freq가 A만 있다면 +1로 계산되어서 블록 뒤에 갯수를 계산함.

'''
# solution
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_freq = max(task_counter.values())
        num_max_freq = sum(1 for v in task_counter.values() if v == max_freq)   # max_freq와 같은 횟수를 가진 문자(v)가 몇개인지 확인하는 코드. 최대값과 같으면 1 아니면 값이 없음.
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max_freq)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task의 빈도 구하기
        task_dict = {}
        for ch in tasks:
            task_dict[ch] = task_dict.get(ch,0)+1

        tmp = []            # 임시로 저장하는 리스트
        p = 0               # tmp내에서 움직이는 포인터
        saved = deque()     # 임시저장 리스트(tmp전용)

        while task_dict or saved :  # task_dict, saved가 둘 다 0이되면 break
            
            if p>=len(tmp):                         # 포인터p가 tmp길이를 벗어나면,
                while saved :                       # saved에 저장해둔 dictionary값을 복원
                    comp= saved.popleft()
                    if comp[1] != 0:                # value가 0이면 패스
                        task_dict[comp[0]] = comp[1]

                if not task_dict :                  # 
                    break
                ch = max(task_dict,key = task_dict.get)
                tmp += [ch] + ['0']*n
                saved = deque([[ch,task_dict[ch]-1]])
                task_dict.pop(ch) 

            else :
                if task_dict :
                    ch = max(task_dict,key = task_dict.get)
                    tmp[p]=ch

                    saved.append([ch,task_dict[ch]-1])
                    task_dict.pop(ch)
                
            p+=1

  
        while tmp :
            if tmp[-1] == '0' :
                tmp.pop()
            else :
                return len(tmp)