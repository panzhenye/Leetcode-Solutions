# 文件名：题号_题目.py (示例：0001_TwoSum.py)
from typing_extensions import List


class Solution:
    def mySolution(self, nums: List[int], target: int) -> List[int]:
        """
        📌 初始解法 | 暴力枚举
        💡 思路：双重循环检查所有组合
        ⏰ 时间复杂度：O(n²)
        🏠 空间复杂度：O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def optimalSolution(self, nums: List[int], target: int) -> List[int]:
        """
        📌 优化解法 | 哈希表
        💡 优化点：空间换时间，查询O(1)
        ⏰ 时间复杂度：O(n)
        🏠 空间复杂度：O(n)
        🔗 参考：LeetCode官方题解
        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i


if __name__ == "__main__":
    sol = Solution()
    cases = (
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 2, 4], 6)
    )
    for case in cases:
        print(sol.mySolution(case[0], case[1]))
        print(sol.optimalSolution(case[0], case[1]))
