from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''用zero_count去记录当前有多少个0，当zero_count>k的时候，移动做指针，直到zero_count<=k'''
        rs = left = zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            rs = max(rs, right - left + 1)
        return rs


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    sol = Solution()
    print(sol.longestOnes(nums, K))
