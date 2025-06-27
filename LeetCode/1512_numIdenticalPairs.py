from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        d = defaultdict(int)
        for i in range(0, len(nums)):
            sum += d[nums[i]]
            d[nums[i]] += 1
        return sum


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    s = Solution()
    print(s.numIdenticalPairs(nums))
