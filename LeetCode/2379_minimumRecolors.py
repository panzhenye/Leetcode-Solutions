class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''先统计前k位得到一个长度为k的窗口，然后使用zip方法去拿到进入窗口和离开窗口的值，计算当前要涂多少个色块，通过min去计算最小的答案'''
        min_white = current = blocks[:k].count('W')
        for incoming, outgoing in zip(blocks[k:], blocks):
            current += (incoming == 'W') - (outgoing == 'W')
            min_white = min(min_white, current)
        return min_white


if __name__ == '__main__':
    blocks = "WBWBBBW"
    k = 2
    sol = Solution()
    rs = sol.minimumRecolors(blocks, k)
    print(rs)
