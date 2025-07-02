'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/valid-anagram/description/

🍊풀이 시간 :
1m

🍒풀이 방법 :
sorted로 해결
Counter함수로 문제를 푸는 경우도 있었음.
other solution은 내 코드보다 속도가 빠름. count함수, for문 자체가 O(N)임. sorted는 정말 주의해서 사용해야할 것 같음

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

# other solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_of_s = {char: s.count(char) for char in set(s)}
        char_count_of_t = {char: t.count(char) for char in set(t)}
        return char_count_of_s == char_count_of_t