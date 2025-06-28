class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''猪脑爆炸都没想出来，看了灵茶山艾府的解析豁然开朗'''
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    n = 16
    sol = Solution()
    print(sol.isPowerOfTwo(n))
