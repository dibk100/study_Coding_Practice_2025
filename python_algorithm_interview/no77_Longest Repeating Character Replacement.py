'''
🍪문제 번호 :
ch20_sliding window
https://leetcode.com/problems/longest-repeating-character-replacement/description/

🍊풀이 시간 :


🍒풀이 방법 :
A,B 문자 두 개만 있어서 가능한 알고리즘
right-left-max를 통해서 그 윈도우 사이즈 안에 k개 이상 바꿔야한다면 left를 움직이는 개념. 
그래서 right-left-max<=k 이기만 하면 right는 사이즈가 커질 수 있구나

'''
def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0

        for right,ch in enumerate(s,1):
            frequency[ch] = frequency.get(ch,0) +1
            
            max_ = max(frequency.values())

            if right - left - max_ > k :
                frequency[s[left]] -=1
                left+=1
        
        return right - left