from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''设定左右两个指针，根据题目的条件，尽可能收缩窗口'''
        left = current = 0
        result = len(nums) + 1  # 初始化为不可能的最大值
        for right in range(len(nums)):
            current += nums[right]
            while current >= target:
                result = min(result, right - left + 1)
                current -= nums[left]
                left += 1
        return result if result <= len(nums) else 0


if __name__ == '__main__':
    target = 15
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))
