from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        '''只要数组的和少于target，就一直加上nums.copy()直到它大于target，然后额外加一组nums.copy()在滑动窗口计算最小的窗口'''
        left = current = 0
        result = float('inf')
        nums_sum = sum(nums)
        if set(nums) == {1}:
            return target
        final_nums = nums.copy()
        finnal_sum = nums_sum
        while finnal_sum < target:
            final_nums += nums.copy()
            finnal_sum += nums_sum
        final_nums += nums.copy()
        finnal_sum += nums_sum
        for right in range(len(final_nums)):
            current += final_nums[right]
            while current > target:
                current -= final_nums[left]
                left += 1
            if current == target:
                result = min(result, right - left + 1)
        return result if result != float('inf') else -1

    def optimalSolution(self, nums: List[int], target: int) -> int:
        '''灵茶山艾府的解决方案，只考虑一头一尾的情况，然后中间有多少个完整的nums使用target // total * n 即可知道，然后对2n进行窗口滑动即可'''
        total = sum(nums)
        n = len(nums)
        ans = float('inf')
        left = s = 0
        rem = target % total
        for right in range(n * 2):
            s += nums[right % n]
            while s > rem:
                s -= nums[left % n]
                left += 1
            if s == rem:
                ans = min(ans, right - left + 1)
        return ans + target // total * n if ans < float('inf') else -1


if __name__ == '__main__':
    nums = [1, 1, 1]
    target = 1000000000
    sol = Solution()
    print(sol.minSizeSubarray(nums, target))
