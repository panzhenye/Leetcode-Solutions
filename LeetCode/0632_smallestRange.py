from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''对nums以及其子数组进行遍历，按照‘(当前数字，所属分组)’格式添加到arr数组，然后对arr进行排序。然后进行窗口滑动,去找满足每一个分组至少要有一个数字在里面，且右指针对应得值减左指针对应的值要最小'''
        arr = []
        for i, num in enumerate(nums):
            for j in num:
                arr.append((j, i))
        arr.sort()
        left = 0
        diff = len(nums)
        diff_arr = [0] * diff
        minial = float('inf')
        res = []
        for right in range(len(arr)):
            diff_arr[arr[right][1]] += 1
            if diff_arr[arr[right][1]] == 1:
                diff -= 1
            while diff == 0:
                num_r = arr[right][0]
                num_l = arr[left][0]
                if num_r - num_l < minial:
                    res = [num_l, num_r]
                    minial = num_r - num_l
                diff_arr[arr[left][1]] -= 1
                if diff_arr[arr[left][1]] == 0:
                    diff += 1
                left += 1
        return res


if __name__ == '__main__':
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    sol = Solution()
    print(sol.smallestRange(nums))
