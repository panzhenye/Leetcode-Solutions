from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        '''题目要求在left和right之间的单词是不是以元音字母开头，按照题目描述的写就好了'''
        s=0
        for i in range(left,right+1):
            word=words[i]
            if word[0] in ('a','e','i','o','u') and word[-1] in ('a','e','i','o','u'):
                s+=1
        return s


if __name__ == '__main__':
    words = ["are", "amy", "u"]
    left = 0
    right = 2
    sol = Solution()
    print(sol.vowelStrings(words, left, right))
