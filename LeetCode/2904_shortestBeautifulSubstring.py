class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        '''先把左右两侧的0剪枝，然后右指针扩张，直到和大于等于k，当和=k，将s[left:right + 1]和result转为10进制数字对比，取较小值（因为题目要求假如两个字符串位置长度相同的情况下，从左往右逐字符比，第一个不同的地方谁的字符大，s的值就越大。就像二进制数字一样）。当和大于k值时，则移动左指针。'''
        left = current = 0
        s = s.lstrip('0').rstrip('0')
        if s.count('1') == k:
            return s
        elif s.count('1') < k:
            return ''
        result = s
        for right in range(len(s)):
            current += int(s[right])
            while current > k or (left < len(s) and s[left] == '0'):
                current -= int(s[left])
                left += 1
            if current == k:
                if int(s[left:right + 1], 2) <= int(result, 2):
                    result = s[left:right + 1]
        return result


if __name__ == '__main__':
    s = "00011001"
    k = 3
    sol = Solution()
    print(sol.shortestBeautifulSubstring(s, k))
