'''
🍪문제 번호 :
ch09_Stack and Queue
https://leetcode.com/problems/remove-duplicate-letters/description/

🍊풀이 시간 :
failed and solve

🍒풀이 방법 :
문제 자체를 잘 이해하지 못해서 1차 실패. 서칭해서 문제를 잘 설명한 블로그를 참고함 https://annajin.tistory.com/130
문자를 중복하지 않아야하고, 사전적 order가 되어야한다는 두 조건을 지켜야 했음. 여기서 문자를 중복하지 않는데, 중복 문자 중 어디 위치의 중복문자를 제거할지 구현하는 것이 핵심 같음.
frequency(dict)를 만들어서 output에 넣을 문자를 확인하는 용도로 활용함. 

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 문자의 빈도 계산 : 확인용
        frequency = {}
        for ch in s :
            frequency[ch] = frequency.get(ch, 0) + 1
        
        # 순차적으로 문자를 확인하며 output에 문자 넣기
        output = []
        for ch in s :
            frequency[ch] -=1      

            if ch in output:        # 중복 문자는 output에 넣거나 확인하지 않고 패스
                continue
            
            # 현재 문자ch가 더 작으면 기존 output문자는 제거
            while output and ch < output[-1] and frequency[output[-1]] >0 :     #  제거 및 비교할 문자(output[-1])가 딕셔너리에 없으면 이제 중복될 문자가 없다는 의미
                output.pop()      

            output.append(ch)       # 뒤에서 추가 : 사전적으로 추가
            
        return output