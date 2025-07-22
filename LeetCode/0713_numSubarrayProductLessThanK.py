from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''这一类题目要求我们去找一个满足该条件的范围，而比该范围小的数组当然更加符合该条件，所以使用ans+=right - left + 1 '''
        if k == 0:
            return 0
        ans = left = 0
        current = 1
        for right in range(len(nums)):
            current *= nums[right]
            while left <= right and current >= k:
                current /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 1
    sol = Solution()
    sol.numSubarrayProductLessThanK(nums, k)
