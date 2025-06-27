class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        sum = 0
        for i in range(0, n):
            sum ^= (start + i * 2)
        return sum


if __name__ == '__main__':
    start = 4
    n = 3
    s = Solution()
    print(s.xorOperation(start, n))
