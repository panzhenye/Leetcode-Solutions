from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        '''这个是超长度也合法的题目，当dic[c]有两个以上时候，即说明有符合条件的一对数，将其加起来即可'''
        ans = left = 0
        dic = defaultdict(int)
        p = 0
        for c in nums:
            dic[c] += 1
            if dic[c] >= 2:
                p += dic[c]-1
            while p >= k:
                dic[nums[left]] -= 1
                p -= dic[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    nums = [3,1,4,3,2,2,4]
    k = 2
    sol = Solution()
    sol.countGood(nums, k)
