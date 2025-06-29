class Solution:
    def isUgly(self, n: int) -> bool:
        '''0231_isPowerOfTwo和0326_isPowerOfThree.py的结合体'''
        while n and n % 3 == 0:
            n //= 3
        while n and n % 5 == 0:
            n //= 5
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    n = 6
    sol = Solution()
    print(sol.isUgly(n))
