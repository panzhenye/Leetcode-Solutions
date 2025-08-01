from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''right-lef范围内都满足条件类型的题目，注意判是断条件是n个值相加再*长度少于k'''
        left = current = sum_num = 0
        for right in range(len(nums)):
            current += nums[right]
            while current * (right - left + 1) >= k:
                current -= nums[left]
                left += 1
            sum_num += right - left + 1
        return sum_num


if __name__ == '__main__':
    nums = [2, 1, 4, 3, 5]
    k = 10
    sol = Solution()
    sol.countSubarrays(nums, k)
