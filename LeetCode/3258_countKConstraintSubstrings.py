from collections import defaultdict


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        '''越短越满足类型题目，使用一个overset去记录大于k的字符，一直扩展右边，当overset超过两个就开始收缩左边，确保条件符合。然后计算每一轮的次数累加即可'''
        ans = left = 0
        dic = defaultdict(int)
        overset = set()
        for right in range(len(s)):
            dic[s[right]] += 1
            if s[right] not in overset and dic[s[right]] > k:
                overset.add(s[right])
            while len(overset) > 1:
                dic[s[left]] -= 1
                if dic[s[left]] <= k:
                    overset.remove(s[left])
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    s = "11111"
    k = 1
    sol = Solution()
    sol.countKConstraintSubstrings(s, k)
