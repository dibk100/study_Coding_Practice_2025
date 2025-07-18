'''
🍪문제 번호 :
ch19_bit
https://leetcode.com/problems/utf-8-validation/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
비트 문제 솔직히 모르겠다. 문제 이해하는데도 시간걸렸고, 풀이도 쉽지 않다.
4byte에서 110xxxxx 10xxxxxx 0xxxxxxx 인데, bin함수 사용할때 자릿수가 맞춰지지 않는다는걸 인식하지 못했음. 0b~이런식으로 출력되니까..
정답 풀이말고 더 쉽게 풀이한 다른 사람 풀이를 찾아서 다시 공부 필요

'''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True

# failed
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        check = bin(data[0])[2:]

        byte = 0
        for c in check :
            if c == '1' :
                byte+=1
            else :
                break
        # byte 체크
        if byte == 0 : return True
        byte -=1

        for d in data[1:] :
            ch = bin(d)[2:4]
            print(bin(d),ch)
            if ch != '10' and byte:
                return False
            else :
                byte -=1
        
        return True