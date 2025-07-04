from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''先获取长度为k的窗口放在数组的最右边，然后一直往右向前推。注意是右边减，左边加'''
        rs = current = sum(cardPoints[-k:])
        for i in range(k):
            current += cardPoints[i] - cardPoints[i - k ]
            rs = max(current, rs)
        return rs


if __name__ == '__main__':
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    sol = Solution()
    p = sol.maxScore(cardPoints, k)
    print(p)
