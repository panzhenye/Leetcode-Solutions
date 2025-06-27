class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        '''低难度题目'''
        if n % 2 == 0:
            return n
        else:
            return n * 2


if __name__ == '__main__':
    n = 29
    sol = Solution()
    print(sol.smallestEvenMultiple(n))
