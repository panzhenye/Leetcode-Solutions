from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        '''低难度题目'''
        return [celsius + float(273.15), celsius * float(1.80) + float(32.00)]


if __name__ == '__main__':
    celsius = 122.11
    sol = Solution()
    print(sol.convertTemperature(celsius))
