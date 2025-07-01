from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        '''
        滑动窗口题，如果k=0，返回原数组即可。因为长度少于i-k到i+k的范围的值都是-1，使用-1填充整个数组。
        然后计算第一个‘窗口’的长度，然后修改数组第k个的值。接着定向滑窗，维护sum的值，修改数组
        '''
        if k == 0:
            return nums.copy()

        # 初始化结果列表，全部填充-1
        result = [-1] * len(nums)
        if k > len(nums):
            return result

        window_size = 2 * k + 1
        if window_size > len(nums):
            return [-1] * len(nums)

        # 计算初始窗口和
        total = sum(nums[:window_size])
        result[k] = total // window_size

        # 使用滑动窗口更新结果
        for right in range(window_size, len(nums)):
            left = right - window_size
            total += nums[right] - nums[left]
            result[left + k + 1] = total // window_size

        return result


if __name__ == '__main__':
    nums = [3, 3]
    k = 0
    sol = Solution()
    rs = sol.getAverages(nums, k)
    print(rs)
