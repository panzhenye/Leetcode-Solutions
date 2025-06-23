from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        📌 初始解法 | 排序然后放进字典，再返回字典的结果
        💡 思路：先将每组字母转为list，然后通过sorted()对list进行排序。然后将排序后的结果作为字典的key值，即可得到相同字母组成的
        """
        d=defaultdict(list)
        for str in strs:
            key = ''.join(sorted(list(str)))
            d[key].append(str)
        return list(d.values())

    def optimalSolution(self, strs: List[str]) -> List[List[str]]:
        '''
        📌 优化解法 | 使用质数相乘，值一样的就说明是由相同的字母组成。
        🔗 参考：改题目的评论区
        '''
        d=defaultdict(list)
        primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                        101]
        for str in strs:
            value=1
            for i in str:
                value*=primeNumbers[ord(i)-ord('a')]
            d[value].append(str)
        return list(d.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    res = sol.groupAnagrams(strs)
    print(res)
    res = sol.optimalSolution(strs)
    print(res)
