from typing import List
from _collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''定一个窗口，然后维护diff、dict和current的变化'''
        rs = 0
        diff = 0
        dict = defaultdict(int)
        current = 0
        for i in nums[:k]:
            if dict[i] == 0:
                diff += 1
            dict[i] += 1
            current += i
        if diff == k:
            rs = max(rs, current)
        for i in range(k , len(nums)):
            dict[nums[i - k]] -= 1
            if dict[nums[i - k]] == 0:
                diff -= 1
            if dict[nums[i]] == 0:
                diff += 1
            dict[nums[i]] += 1

            current += nums[i] - nums[i - k]
            if diff == k:
                rs = max(rs, current)
        return rs


if __name__ == '__main__':
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    sol = Solution()
    p = sol.maximumSubarraySum(nums, k)
    print(p)
