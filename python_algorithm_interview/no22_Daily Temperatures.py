'''
🍪문제 번호 :
ch09_Stack and Queue
https://leetcode.com/problems/daily-temperatures/description/

🍊풀이 시간 :
15m failed

🍒풀이 방법 :
failed - two pointer로 if문 체크하며 계산하려고 했으나, testcase에서 몇 개 이슈가 생기며 지저분한 코드가 됨. -> 순서 바꾸면 가능할 거 같은데? -> 35testcase에서 timeout
>> 어차피 안될 풀이었는데 빨리 포기나하지..

이중 for문을 사용해야하나 고민했는데, 인덱스 위치를 활용해서 거리값을 구함. 그리고 pop을 통해서 시간 복잡도도 확보함. 
해당 솔루션 암기하기~

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left,right = 0,1
        day = 0
        days = len(temperatures)
        result = [0]*days

        while right < days:
            if temperatures[left] < temperatures[right] :
                result[left] = day+1
                left+=1
                right=left+1
                day =0
            elif temperatures[left] >= temperatures[right] :
                if right == days-1 and left < days-2 :
                    left +=1
                    right = left
                    day = -1
                    
                right+=1
                day+=1
        
        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        tmp = []                                                # index를 담아두는 공간
        
        for ind,cur_t in enumerate(temperatures) :
            
            while tmp and cur_t > temperatures[tmp[-1]] :   # tmp
                save_idx = tmp.pop()
                result[save_idx] = ind-save_idx
            
            tmp.append(ind)
        
        return result