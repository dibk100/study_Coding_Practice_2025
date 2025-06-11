'''
🍪문제 번호 :
ch17_sort
https://leetcode.com/problems/merge-intervals/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
굉장히 그리디하게 풀었지만 실패. intervals를 정렬하고 for해야한다는 걸 test case 통해 뒤 늦게 확인함.
풀이를 보는데 이렇게 단순해도 되나?ㅜ max를 사용하면 되는 간단한 풀이.

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:           # result[-1][1] : 맨 뒤의 end값이 interval start보다 작으면
                result.append(interval)
            else:
                result[-1][1] = max(                                # 맨 뒤의 end값과 interval의 end값 비교
                    result[-1][1],
                    interval[1]
                )

        return result