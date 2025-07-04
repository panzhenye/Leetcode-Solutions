from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''定向滑窗，不同的是，这次先计算老板生气会丢失多少顾客，记录丢失顾客最多的那个sid（该范围的开始id），然后把连续n分钟不生气放在sid那个范围，即可挽留最多的顾客'''
        lost_cus = [a * b for a, b in zip([i for i in grumpy], customers)]
        max_cus = current = sum(lost_cus[:minutes])
        sid = 0
        for i in range(minutes, len(lost_cus)):
            current += lost_cus[i] - lost_cus[i - minutes]
            if current >= max_cus:
                sid = i - minutes + 1
            max_cus = max(max_cus, current)
        print(grumpy[sid:sid + minutes])
        grumpy[sid:sid + minutes] = [0] * minutes
        rs = sum([a * (b ^ 1) for a, b in zip(customers, grumpy)])
        return rs


if __name__ == '__main__':
    customers = [4, 10, 10]
    grumpy = [1, 1, 0]

    minutes = 2
    sol = Solution()
    p = sol.maxSatisfied(customers, grumpy, minutes)
    print(p)
