from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # 先去重再排序
        max_num = count = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
                max_num = max(max_num, count)
            else:
                count = 1

        return max_num

    def optimalSolution(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # 只有当 num 是序列的起点时才进入循环（避免重复计算）
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # 向后扩展序列
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    s = Solution()
    print(s.longestConsecutive(nums))
    print(s.optimalSolution(nums))
