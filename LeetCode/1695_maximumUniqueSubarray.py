from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''滑动窗口，每轮右边加1，同时维护current（当前这一轮的和）的值，和rs的值（结果，即最大值），同时每一轮都检查是否有重复，有重复的就不断右移左边的指针，直到没重复的值'''
        rs = current = left = right = 0
        s = set()
        while right < len(nums):
            while nums[right] in s:
                current -= nums[left]
                s.remove(nums[left])
                left += 1
            current += nums[right]
            rs = max(rs, current)
            s.add(nums[right])
            right += 1
        return rs


if __name__ == '__main__':
    nums = [4, 2, 4, 5, 6]
    sol = Solution()
    print(sol.maximumUniqueSubarray(nums))
