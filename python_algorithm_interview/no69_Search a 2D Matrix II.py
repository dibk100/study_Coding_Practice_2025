'''
🍪문제 번호 :
ch18_binary_search
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
조건의 패턴을 찾아서 알고리즘 구현해야하는 문제로 인식
- 그리디 알고리즘(모든 맵을 확인하며 이동해야함) -> 너무 코드가 구려짐

이 문제의 key point는 행을 기준으로 잡고, 가장 큰 값에서 비교하며 작아지는 순으로 체크했어야 했음
나는 처음부터 행과 열을 잡고 한번에 진행하려고 알고리즘을 고민해서 문제를 푸는데 시간이 많이 걸렸음.

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        x,y = 0,col-1
        while x >= 0 and x < row and y >= 0 and y < col :

            if matrix[x][y] == target :
                return True
            
            elif matrix[x][y] < target :
                x +=1
            
            else :
                y -=1

        return False

        