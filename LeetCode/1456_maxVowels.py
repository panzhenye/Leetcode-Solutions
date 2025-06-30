class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''一开始的思路是每次取指定的长度k的数据进行统计，每循环一次就取k长度取统计，这样效率太低了，超时了。
        后面想起之前做过定向滑窗的题目，就按照定向滑窗的题目去做：1、统计前k个字符串拥有都少个元音字母，然后for循环剩下的数据，即k到len(s)
        这样我们只要维护count的值，关注一头（i-k）一尾(i)是不是元音字母进行加减即可。
        '''
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = current = sum(1 for char in s[:k] if char in vowels)
        for i in range(k, len(s)):
            current += (s[i] in vowels) - (s[i - k] in vowels)
            max_count = max(max_count, current)
        return max_count


if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    sol = Solution()
    print(sol.maxVowels(s, k))
