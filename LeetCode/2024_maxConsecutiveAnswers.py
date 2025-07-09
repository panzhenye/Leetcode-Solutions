class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''双指针，左指针移动的条件是：当右指针添加进字典后，字典中的T和F的值的最小值大于k即移动做指针'''
        rs = left = 0
        d = {'T': 0, 'F': 0}
        for right in range(len(answerKey)):
            d[answerKey[right]] += 1
            while d['T'] > k and d['F'] > k:
                d[answerKey[left]] -= 1
                left += 1
            rs = max(rs, right - left + 1)
        return rs


if __name__ == '__main__':
    answerKey = "FTFTFTFT"
    k = 1
    sol = Solution()
    print(sol.maxConsecutiveAnswers(answerKey, k))
