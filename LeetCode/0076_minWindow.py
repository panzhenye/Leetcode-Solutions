from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''通过判断t字典“td”里面所有的值都小于等于0，即移动左指针实现目的，效率较低'''
        left = 0
        td = defaultdict(int)
        ans_num = float('inf')
        ans = ''
        for i in t:
            td[i] += 1
        for right in range(len(s)):
            while all(td[i] <= 0 for i in t) or (left <= right and s[left] not in td) or (
                    left <= right and td[s[left]] < 0):
                if s[left] in td:
                    td[s[left]] += 1
                left += 1
            if s[right] in td:
                td[s[right]] -= 1
            if all(td[i] <= 0 for i in t):
                if ans_num >= right - left + 1:
                    ans = s[left:right + 1]
                ans_num = min(ans_num, right - left + 1)
        return ans

    def optimalSolution(self, s: str, t: str) -> str:
        '''chatgpt给的方案，通过维护一个required去判断不通字符数量决定左指针移动，效率高一点'''
        if not t or not s:
            return ""

        td = Counter(t)
        window = defaultdict(int)

        required = len(td)  # 不同字符的个数
        formed = 0

        l = 0
        ans = float('inf'), None, None  # 长度, 左, 右

        for r, char in enumerate(s):
            window[char] += 1

            if char in td and window[char] == td[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window[s[l]] -= 1
                if s[l] in td and window[s[l]] < td[s[l]]:
                    formed -= 1
                l += 1

        if ans[0] == float('inf'):
            return ""
        return s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.optimalSolution(s, t))
