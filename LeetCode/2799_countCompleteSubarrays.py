from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        '''求符合条件的子数组题目，通过累加符合条件的left的值即可得到结果'''
        ans = left = 0
        dict = defaultdict(int)
        n = len(set(nums))
        for c in nums:
            dict[c] += 1
            while len(dict) >= n:
                dict[nums[left]] -= 1
                if dict[nums[left]] == 0:
                    del dict[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    nums = [1, 3, 1, 2, 2]
    sol = Solution()
    sol.countCompleteSubarrays(nums)
