from collections import defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        '''只要指定的字母出现了，就算有多个有多余的字符也满足条件的类型的题目。使用两个字典对比，第一个为条件字典condict，第二个为当前字典currendict。
        以条件字典的长度n表示存在n个不同的字符。当两个字典的某个字符相等时。n减1.一直向右扩展，直到满足n==0，满足n后不断，收缩左边，直到不满足n==0
        然后通过累加left的值即可得到总次数'''
        left = ans = 0
        currendict = defaultdict(int)
        condict = defaultdict(int)
        for c in word2:
            condict[c] += 1
        n = len(condict)
        for c in word1:
            currendict[c] += 1
            if c in condict and currendict[c] == condict[c]:
                n -= 1
            while n == 0:
                currendict[word1[left]] -= 1
                if word1[left] in condict and currendict[word1[left]] < condict[word1[left]]:
                    n += 1
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    word1 = "eeddeeded"
    word2 = "dde"
    sol = Solution()
    sol.validSubstringCount(word1, word2)
