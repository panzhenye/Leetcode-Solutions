from typing import List
from _collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        '''截取一段，然后set判重，然后看有没有大过m，如果大于m，就计算result'''
        result = 0
        for i in range(k, len(nums) + 1):
            if len(set(nums[i - k:i])) >= m:
                result = max(result, sum(nums[i - k:i]))
        return result

    def optimalSolution(self, nums: List[int], m: int, k: int) -> int:
        '''维护k长度的窗口，对比window_sum、unique和dict的变化'''
        result = 0
        dict = defaultdict(int)
        unique = 0
        window_sum = 0
        for i in nums[:k]:
            if dict[i] == 0:
                unique += 1
            dict[i] += 1
            window_sum += i
        if unique >= m:
            result = max(result, window_sum)
        for i in range(k, len(nums)):
            dict[nums[i - k]] -= 1
            if dict[nums[i - k]] == 0:
                unique -= 1
            if dict[nums[i]] == 0:
                unique += 1
            dict[nums[i]] += 1
            window_sum+=nums[i]-nums[i-k]
            if unique >= m:
                result = max(result, window_sum)
        return result


if __name__ == '__main__':
    nums = [1,1,1,3]
    m = 2
    k = 2
    sol = Solution()
    rs = sol.optimalSolution(nums, m, k)
    print(rs)
