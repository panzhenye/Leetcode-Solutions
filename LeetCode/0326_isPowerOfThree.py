class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return n == 1

if __name__ == '__main__':
    n=27
    sol=Solution()
    print(sol.isPowerOfThree(n))