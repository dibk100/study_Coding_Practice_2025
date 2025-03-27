'''
🍪문제 번호 :
ch07_Array
https://leetcode.com/problems/two-sum/description/

🍊풀이 시간 :
30m(failed)

🍒풀이 방법 :
단순하게 생각하면 브루스포트, 더 깊게 생각하면 two-pointer, 더 꼬아 생각하면 중간 위치부터 확인하는 작업 but 실패
문제를 잘 읽어보면 인풋 데이터는 음수도 가능하고, 리턴 값이 인덱스. 이 부분을 고민하고 작성했으면 좋았을 것 같음.

딕셔너리 기법은 다른 풀이에서도 유용하게 활용 될 것 같음.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for idx_ in range(len(nums)):
            val_ = target -nums[idx_] 
            if val_ in dict_.keys():
                return [dict_[val_], idx_]
            
            dict_[nums[idx_]] = idx_
        
        return []