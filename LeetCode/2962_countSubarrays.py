from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''当不满足条件的时候，滑动右边，当满足条件之后，一直滑动左边，知道不满住。每一轮左边的值加起来就是合计的次数。因为右边满足了，左边的数存不存在都会满足这个情况的'''
        left = ans = current = 0
        target = max(nums)
        for c in nums:
            if c == target:
                current += 1
            while current >= k:
                if nums[left] == target:
                    current -= 1
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 3]
    k = 2
    sol = Solution()
    sol.countSubarrays(nums, k)
