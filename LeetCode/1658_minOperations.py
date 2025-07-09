from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''逆向思维，改为求sum(num)-x的最大长度，当其为最长的时候，说明x的长度是最短的'''
        left = current = rs = 0
        condition = sum(nums) - x
        if condition < 0:
            return -1
        if condition == 0:
            return len(nums)
        for right in range(len(nums)):
            current += nums[right]
            while current > condition:
                current -= nums[left]
                left += 1
            if current == condition:
                rs = max(rs, right - left + 1)
        return -1 if rs == 0 else len(nums) - rs


if __name__ == '__main__':
    nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
    x = 134365
    sol = Solution()
    print(sol.minOperations(nums, x))
