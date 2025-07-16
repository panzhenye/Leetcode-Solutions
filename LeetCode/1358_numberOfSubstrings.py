from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''使用了窗口滑动方法，只有符合条件，abc都存在字串的时候，left才会进行收缩，所以每一轮都加上left的值，而且有多少种情况是看left前面有多少个字符'''
        ans = 0
        left = 0
        dic = defaultdict(int)
        for right in range(len(s)):
            dic[s[right]] += 1
            while len(dic) == 3:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    s = "acbbcac"
    sol = Solution()
    sol.numberOfSubstrings(s)
