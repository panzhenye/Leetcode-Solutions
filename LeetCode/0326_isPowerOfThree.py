class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''当 n 不为零且能被 3 整除时，一直循环，看最后n是不是1'''
        while n and n % 3 == 0:
            n //= 3
        return n == 1

if __name__ == '__main__':
    n=12
    sol=Solution()
    print(sol.isPowerOfThree(n))