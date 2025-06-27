from collections import defaultdict, Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''想了一下没做出来，第一次做前缀和的题目，学习了。答案参考灵茶山艾府的。
        大概思路是先用循环求出数组前n位的和。然后相减求出差值，如果值刚好为k，即说明有连续的n个值的和刚好是k
        以[4, 1, 2, 3]为例子。假如k是6
        肉眼可以看见1+2+3的值刚好是6
        先用循环求和。那么我们得到的数组是这样的↓
        [4(0+4),5(4+1),7(4+1+2),10(4,1,2,3)]
        假如我们用数组的最后一个值减去第一个值，即可得到后三位连续的数的和，即[1,2,3]
        '''
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        ans = 0
        cnt = defaultdict(int)
        for j in s:
            ans += cnt[j - k]
            cnt[j] += 1
        return ans

    def optimalSolution(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # s[0]=0 单独统计
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans


if __name__ == '__main__':
    nums = [4, 1, 2, 3, 0, 6, 2, 4]
    k = 6
    solution = Solution()
    print(solution.optimalSolution(nums, k))
