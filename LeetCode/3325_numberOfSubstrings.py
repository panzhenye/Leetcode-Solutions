from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        '''前面符合要求的组数和left的位置有关，也就是说left前面肯定存在若干组符合条件的字串，加起来就算答案'''
        left = ans = 0
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
            while dic[c] >= k:
                dic[s[left]] -= 1
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    s = "abacb"
    k = 2
    sol = Solution()
    sol.numberOfSubstrings(s, k)
