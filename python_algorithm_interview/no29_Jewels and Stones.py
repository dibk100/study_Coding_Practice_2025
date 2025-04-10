'''
🍪문제 번호 :
ch11_Hash Table
https://leetcode.com/problems/jewels-and-stones/description/

🍊풀이 시간 :
5m

🍒풀이 방법 :
jewel을 기준으로 stones의 돌을 카운팅하는 문제.
예전에 작성했던 코드를 비교해봤는데, jewels_d를 {j for j in jewels}로 작성했었다.
더 간결한 코드였지만 시간복잡도는 현재 코드가 더 빠르다.
예전 작성 코드로 제출해도 통과지만, 시간복잡도를 고려한다면 현재 코드가 더 굳.

해시 테이블의 특징을 확연히 느끼게 됨.
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_d = {}
        for j in jewels :
            jewels_d[j] = jewels_d.get(j,0) + 1
        
        result = 0
        for s in stones :
            if s in jewels_d.keys() :
                result +=1