from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''典型的双指针，只是左指针移动的逻辑不一样而已'''
        left = right = current = rs = 0
        d = defaultdict(int)
        while right < len(nums):
            while d[nums[right]] >= k:
                d[nums[left]] -= 1
                current -= 1
                left += 1
            d[nums[right]] += 1
            current += 1
            rs = max(current, rs)
            right += 1
        return rs


if __name__ == '__main__':
    nums = [5,5,5,5,5,5,5]
    k = 4
    sol = Solution()
    print(sol.maxSubarrayLength(nums, k))
