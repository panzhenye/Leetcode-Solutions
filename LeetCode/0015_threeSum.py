from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> list[int] | list[list[int]]:
        '''
        这题想了很久没做出来，参考了评论区的思路写了出来。一开始用暴力循环跑结果，超时了。后面又在纠结怎么判重，没想到先对数组进行排序。
        '''
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_num = nums[i] + nums[left] + nums[right]
                if sum_num == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                elif sum_num < 0:
                    left += 1
                else:
                    right -= 1
        return result

    def optimalSolution(self, nums: List[int]) -> list[int] | list[list[int]]:
        '''
        后面问了下deepseek，边界处理更好，更完善。
        '''
        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        # 快速判断全正或全负
        if nums[0] > 0 or nums[-1] < 0:
            return []

        result = []

        for i in range(n - 2):
            # 提前终止条件
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 更严格的提前终止
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过所有重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 同时移动两个指针
                    left += 1
                    right -= 1

        return result

if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    s = Solution()
    print(s.threeSum(nums))
