from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''第一反应想起0049的一个骚套路，用质素相乘法去判断是不是异位词，然后结合0003滑动窗口得出来的。但是测试案例33给了一个超长的参数，结果超时了(-_-)。老老实实在优化方案用哈希来实现'''
        if not s:
            return 0
        primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                        101]
        ans = []
        lens = len(s)
        lenp = len(p)
        matchValue = 1
        for i in p:
            matchValue *= primeNumbers[ord(i) - ord('a')]
            print(matchValue)
        for i in range(lens - lenp + 1):
            value = 1
            j = i
            while j < i + lenp:
                value *= primeNumbers[ord(s[j]) - ord('a')]
                j += 1
            if value == matchValue:
                ans.append(i)
        return ans

    def optimalSolution(self, s: str, p: str) -> List[int]:
        '''遍历s，每次截取p一样的长度，然后对其排序然后和p对比，一样就记录下来'''
        if not s:
            return 0
        p = ''.join(sorted(p))
        ans = []
        lens = len(s)
        lenp = len(p)
        sorted(p)
        for i in range(lens - lenp + 1):
            if ''.join(sorted(s[i:i + lenp])) == p:
                ans.append(i)
        return ans

    def optimalSolution2(self, s: str, p: str) -> List[int]:
        """参考官方题解，p，s分别用两个数组取记录每个字母的数量，在遍历的时候不断移出左边的字母（在s数组减去该字母），移入右边的字母（s数组该字母的位置加1），然后和p数组对比确定是否一样"""
        s_len, p_len = len(s), len(p)

        # 边界条件处理
        if s_len < p_len or p_len == 0:
            return []
        # 初始化字母计数数组（只包含小写字母）
        s_count = [0] * 26  # 当前窗口的字母计数
        p_count = [0] * 26  # 目标模式p的字母计数

        # 初始化第一个窗口和p的字母计数
        for i in range(p_len):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
        result = []

        # 检查初始窗口是否匹配
        if s_count == p_count:
            result.append(0)
        # 滑动窗口遍历剩余字符串
        for window_start in range(s_len - p_len):
            # 移出窗口的字符（左侧）
            left_char = s[window_start]
            s_count[ord(left_char) - ord('a')] -= 1

            # 移入窗口的字符（右侧）
            right_char = s[window_start + p_len]
            s_count[ord(right_char) - ord('a')] += 1

            # 检查当前窗口是否匹配
            if s_count == p_count:
                result.append(window_start + 1)  # 记录新窗口的起始位置
        return result

    def optimalSolution3(self, s: str, p: str) -> List[int]:
        '''和优化方案2差不多，只不过它只用一个数组取实现，当所有值都是0的时候说明是由相同字母组成的，另外精巧地利用一个differ_count去记录有多少个字母不同'''
        # 定义字母表大小和ASCII偏移量
        ALPHABET_SIZE = 26
        ASCII_OFFSET = ord('a')

        s_len, p_len = len(s), len(p)

        # 如果s比p短，直接返回空列表
        if s_len < p_len:
            return []

        result = []
        # 初始化计数数组，记录s和p中字母的频率差
        freq_diff = [0] * ALPHABET_SIZE

        # 初始化第一个窗口
        for i in range(p_len):
            freq_diff[ord(s[i]) - ASCII_OFFSET] += 1  # 增加s中的字母计数
            freq_diff[ord(p[i]) - ASCII_OFFSET] -= 1  # 减少p中的字母计数

        # 计算初始差异数（有多少字母的频率不同）
        differ_count = sum(1 for count in freq_diff if count != 0)

        # 如果初始窗口就是变位词
        if differ_count == 0:
            result.append(0)

        # 滑动窗口遍历s
        for i in range(s_len - p_len):
            left_char = s[i]  # 窗口左侧即将移出的字符
            right_char = s[i + p_len]  # 窗口右侧即将移入的字符

            # 处理左侧移出的字符
            if freq_diff[ord(left_char) - ASCII_OFFSET] == 1:  # 移出后该字母频率匹配
                differ_count -= 1
            elif freq_diff[ord(left_char) - ASCII_OFFSET] == 0:  # 移出前匹配，移出后不匹配
                differ_count += 1
            freq_diff[ord(left_char) - ASCII_OFFSET] -= 1

            # 处理右侧移入的字符
            if freq_diff[ord(right_char) - ASCII_OFFSET] == -1:  # 移入后该字母频率匹配
                differ_count -= 1
            elif freq_diff[ord(right_char) - ASCII_OFFSET] == 0:  # 移入前匹配，移入后不匹配
                differ_count += 1
            freq_diff[ord(right_char) - ASCII_OFFSET] += 1

            # 如果所有字母频率都匹配，记录起始位置
            if differ_count == 0:
                result.append(i + 1)

        return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "acb"
    solution = Solution()
    print(solution.optimalSolution3(s, p))
