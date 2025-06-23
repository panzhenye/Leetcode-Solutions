from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        设置两个指针，一个放在左边一个放在右边。计算其面积，然后用max_area去记录最大的面积。然后对比数组中左右两边较小的那个数字（左值右移，右值左移）
        '''
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def optimalSolution(self, height: List[int]) -> int:
        '''
        这个大致和上面差不多，但是加了一个退出的条件。假如 height数组中最大那个值*(right - left)依然比max_area小，那就退出循环
        '''
        left = 0
        right = len(height) - 1
        max_h = max(height) #数组的最大值
        max_area = 0
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_area > max_h * (right - left):   #退出循环的条件
                break
        return max_area


if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(nums)
