'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/group-anagrams/description/

🍊풀이 시간 :
7m

🍒풀이 방법 :
입력 값(str)에서 문자값 빈도 계산 후, 입력값 딕셔너리를 만들고 딕셔너리끼리 비교하려고 했음. -> 복잡하고 비효율적
입력값(str)을 sort해서 key값으로 만들고 원값(입력값)을 value값으로 저장.

0 <= strs[i].length <= 100
위 제약조건이라서 sort함수 사용 가능하다고 판단
'''

class Solution:
    def groupAnagrams(self, strs : List[str]) -> List[List[str]] :
        output = {}
        
        for word in strs :
            key = ''.join(sorted(word))
            output[key] = output.get(key,[]) + [word]
        
        return [val for val in output.values()]
