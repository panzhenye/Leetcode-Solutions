class Solution:
    def maxScore(self, s: str) -> int:
        '''不是很复杂'''
        rs = 0
        for i in range(1, len(s)):
            rs = max(rs, s[0:i].count('0') + s[i:len(s)].count('1'))
        return rs


if __name__ == '__main__':
    s = "011101"
    sol = Solution()
    print(sol.maxScore(s))
