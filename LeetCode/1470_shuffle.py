from typing import List


class Solution:
    '''观察题目数组，n刚好是数组的一半，x1和y1刚好相差n'''

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        rs = []
        for i in range(0, n):
            rs.append(nums[i])
            rs.append(nums[i + n])
        return rs


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    sol = Solution()
    print(sol.shuffle(nums, n))
