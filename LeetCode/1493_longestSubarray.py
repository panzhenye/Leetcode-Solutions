from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        rs = 0
        while right<len(nums):
            if nums[right] == 0:
                temp_right = right + 1
                while temp_right<len(nums) and nums[temp_right] == 1:
                    temp_right += 1
                current = temp_right - left-1
                rs = max(rs, current)
                left=right+1
            right += 1
        if right==len(nums) and left==0:
            return right-1
        return rs


if __name__ == '__main__':
    nums = [1,1,1]
    sol = Solution()
    sol.longestSubarray(nums)
