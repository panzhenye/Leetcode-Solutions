from collections import Counter
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        '''滑动窗口越小越合适类型题目。使用counter去记录数据，然后对比counter里面最大值-最小值是否大于2，大于2则收缩左边。'''
        left = ans = 0
        cnt = Counter()
        for right in range(len(nums)):
            cnt[nums[right]] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    nums = [5, 4, 2, 4]
    sol = Solution()
    sol.continuousSubarrays(nums)
