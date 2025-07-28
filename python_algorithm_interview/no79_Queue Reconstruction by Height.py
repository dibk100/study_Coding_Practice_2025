'''
🍪문제 번호 :
ch21
https://leetcode.com/problems/queue-reconstruction-by-height/

🍊풀이 시간 :


🍒풀이 방법 :
1. 정렬하기. k작은순, h작은 순
2. 공간 만들기
3. for문 체크

이 방법보다 처음에 생각했던, k를 기준으로 위치를 잡고, h를 큰 수로 정렬해서 밀려나게 하는 게 더 쉽게 구현됨.

'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))      
        print(people)

        output=[]          
        for a in people:
            output.insert(a[1], a)
        
        return output  