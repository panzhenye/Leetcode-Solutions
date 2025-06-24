from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        错误思路示范，一直想着去遍历、比较两边较矮的那个柱子，结果超时了
        '''
        left, right = 0, 1
        total = 0
        while right < len(height) - 1:
            if height[left] < height[right]:
                if right - left == 1:
                    left += 1
                    right += 1
                else:
                    left += 1
            else:
                flag = 0
                h = 0
                maxi = 0
                for i in range(right + 1, len(height)):
                    if height[right] < height[left] < height[i]:
                        flag = 1
                        h = height[left]
                        break
                    elif height[left] >= height[i] > height[right]:
                        if height[i] > maxi:
                            flag = 1
                            h = height[i]
                            maxi = h
                    else:
                        continue
                if flag == 1:
                    total += h - height[right]
                    right += 1
                else:
                    right += 1
        return total

    def optimalSolution(self, height: List[int]) -> int:
        '''
        看了一下评论区的思路，两边往中间算，然后记录两边的最大值。
        :param height:
        :return:
        '''
        left, right = 0, len(height) - 1
        lh = rh = 0
        total = 0
        while left < right:
            lh = max(lh, height[left])
            rh = max(rh, height[right])
            if lh < rh:
                total += lh - height[left]
                left += 1
            else:
                total += rh - height[right]
                right -= 1
        return total

    def optimalSolution2(self, height: List[int]) -> int:
        '''
        动态规划解法，参考官方题解
        :param height:
        :return:
        '''
        if not height:
            return 0
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, - 1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

    def optimalSolution3(self, height: List[int]) -> int:
        '''评论区看到更好的算法，对比两边的指针的大小，根据小的一边确定可以装多少水，学习了'''
        ans = 0
        left = 0
        right = len(height) - 1
        pre_max = 0
        suf_max = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    nums = [4, 2, 0, 3, 2, 5]
    s = Solution()
    rs = s.optimalSolution3(nums)
    print(rs)
