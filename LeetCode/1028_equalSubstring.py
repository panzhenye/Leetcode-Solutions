class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        '''先用一个diff求出差值，然后双指针去找当前预算下最大长度'''
        diff = []
        for i in range(len(s)):
            diff.append(abs(ord(s[i]) - ord(t[i])))
        left = right = current=rs = 0
        while right < len(diff):
            current += diff[right]
            if current <= maxCost:
                rs = max(rs, right - left+1)
            else:
                current -= diff[left]
                left += 1

            right += 1
        return rs

    def optimalSolution(self, s: str, t: str, maxCost: int) -> int:
        '''优化点删除了diff，边找变计算，找出最大的长度。这个方法节省了空间，少了一轮计算diff的时间'''
        left = right = current = rs = 0
        while right < len(s):
            current += abs(ord(s[right]) - ord(t[right]))
            if current <= maxCost:
                rs = max(rs, right - left + 1)
            else:
                current -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            right += 1
        return rs



if __name__ == '__main__':
    s = "aaaabcdef"
    t = "aaabxxxxxx"
    mc = 3
    sol = Solution()
    print(sol.optimalSolution(s, t, mc))
