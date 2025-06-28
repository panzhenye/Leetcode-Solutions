class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num

    def optimalSolution(self, num: int) -> int:
        '''数字根的数学性质：任何数字的数根等于它除以9的余数（当余数不为0时）,来自deepseek的解法'''
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

if __name__ == '__main__':
    nums = 1
    sol = Solution()
    print(sol.optimalSolution(nums))
