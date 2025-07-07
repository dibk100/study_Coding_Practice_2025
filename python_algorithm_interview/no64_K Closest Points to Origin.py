'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/k-closest-points-to-origin/

🍊풀이 시간 :
20m

🍒풀이 방법 :
이렇게 오래걸릴 문제였을지 모르겠음.
answer 루프 돌 때, append가 아닌 extend로 활용할 것.
한 번에 할 수 있는 코드로 더 고민할 것

'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculation(x,y):
            return (x**2 + y**2)**(1/2)
        
        result = {}
        for x,y in points :
            dist = calculation(x,y)

            if dist not in result :
                result[dist] = [[x,y]]
            else :
                result[dist] += [x,y],
        
        answer = []
        for key,value in sorted(result.items())[:k]:
            answer.extend(value)
        
        return answer[:k]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x:x[0]**2+x[1]**2)[:k]
