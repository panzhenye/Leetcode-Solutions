from collections import defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        '''题目的意思是你只能替换指定长度的字符串（意思要连续），替换完之后要让所有的字母平衡。换句话说就是你用两个
        指针去测试，当去除你从左到右指针那个范围，数据还满不满足QWER都小于s/4的长度（因为左到右的范围可以任意变）
        然后找到最短的左到右的长度就可以了。这题让人感到难的是题目的描述很绕，然后测试案例选得不好'''
        result = len(s) + 1
        left = 0
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        avg = int(len(s) / 4)
        for i in s:
            counter[i] += 1
        if len(s) == 4:
            result = 0
            for i in counter.keys():
                if counter[i] < avg:
                    result += avg - counter[i]
            return result
        if counter['Q'] == counter['W'] == counter['E'] == counter['R']:
            return 0
        for right in range(len(s)):
            counter[s[right]] -= 1
            while left < right and counter['Q'] <= avg and counter['W'] <= avg and counter['E'] <= avg and counter[
                'R'] <= avg:
                result = min(result, right - left + 1)
                counter[s[left]] += 1
                left += 1
        return result


if __name__ == '__main__':
    s = "RQQERWEWWREQEQWR"
    sol = Solution()
    print(sol.balancedString(s))
