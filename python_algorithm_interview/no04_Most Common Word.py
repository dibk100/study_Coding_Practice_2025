'''
🍪문제 번호 :
ch06_String_Manipulation
https://leetcode.com/problems/most-common-word/description/

🍊풀이 시간 :
14m

🍒풀이 방법 :
*collections Counter 라이브러리 사용하지 않고 re 사용하지 않고 풀어볼랬는데, 구두점 이슈로 문자열 전처리 코드 생각하는데 시간이 걸렸음. 결국 re 라이브러리 사용.
딕셔너리 초기화할 때, get함수 활용하면 좋은 것 같음.

혹시 모르니 Counter함수 활용
'''
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-zA-Z0-9]',' ',paragraph)
        paragraph = [word.lower() for word in paragraph.split()]
        output = {}

        for word in paragraph:
            if word in banned :
                continue
            
            output[word] = output.get(word,0) +1

        return max(output,key=output.get)
    
    def mostCommonword(self,paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^\w]',' ',paragraph)
        counter = Counter([word.lower() for word in paragraph.split() if word.lower() not in banned])
        return counter.most_common(1)[0][0]


        