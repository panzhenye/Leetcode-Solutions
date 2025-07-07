from typing import List
from _collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = rs = 0
        d = defaultdict(int)
        while right < len(fruits):
            d[fruits[right]] += 1
            if len(d.keys()) <= 2:
                current = right - left + 1
                rs = max(rs, current)
            else:
                while len(d.keys()) > 2:
                    d[fruits[left]] -= 1
                    if d[fruits[left]] == 0:
                        del d[fruits[left]]
                    left += 1
            right += 1
        return rs

    def optimalSolution(self, fruits: List[int]) -> int:
        left = right = rs = 0
        d = defaultdict(int)
        while right < len(fruits):
            d[fruits[right]] += 1
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            current = right - left + 1
            rs = max(rs, current)
            right += 1
        return rs


if __name__ == '__main__':
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    sol = Solution()
    print(sol.optimalSolution(fruits))
