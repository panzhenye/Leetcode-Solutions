class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''直接暴力解法跑出来'''
        ans = 0
        n = len(s)
        for index, letter in enumerate(s):
            text = ''
            num = index
            while num < n and s[num] not in text:
                text += s[num]
                ans = max(ans, len(text))
                num = num + 1
        return ans

    def optimalSolution(self, s: str) -> int:
        '''只要出现重复的，就开始从左边删，直到没重复为止。然后再次添加'''
        if not s:
            return 0
        ans = 0
        n = len(s)
        letterSet = set()
        left = 0
        for i in range(n):
            while s[i] in letterSet:
                letterSet.remove(s[left])
                left += 1
            letterSet.add(s[i])
            ans = max(ans, len(letterSet))
        return ans


if __name__ == '__main__':
    s = 'pwwkew'
    solution = Solution()
    print(solution.optimalSolution(s))
