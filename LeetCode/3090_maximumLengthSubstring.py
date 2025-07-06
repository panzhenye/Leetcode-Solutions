from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''维护左右两个指针，题目说不能超过两个相同的字母，用一个dict去记录，只要超了两个，就一直从左边删除，直到少于两个位置，然后每轮统计最大值'''
        counter = defaultdict(int)
        rs = 0
        left = right = 0
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 2:
                counter[s[left]] -= 1
                left += 1
            current = right - left + 1
            rs = max(rs, current)
            right += 1
        return rs


if __name__ == '__main__':
    s = "aaaa"
    sol = Solution()
    sol.maximumLengthSubstring(s)
