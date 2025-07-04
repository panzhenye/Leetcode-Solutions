from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''按照给的条件来写，但是每次sum(list)效率有点低，这时候我们要考虑定向滑窗减少计算，提升效率'''
        rs = []
        for i in range(len(code)):
            if k >= 0:
                if abs(k) <= i + k + 1 <= len(code):
                    rs.append(sum(code[(i + 1):(i + k + 1)]))
                else:
                    rs.append(sum(code[(i + 1):]) + sum(code[:(i + k + 1 - len(code))]))
            if k < 0:
                if i + k < 0:
                    print(code[i + k:], code[:i])
                    rs.append(sum(code[i + k:]) + sum(code[:i]))
                else:
                    rs.append(sum(code[i + k:i]))
        return rs

    def optimalSolution(self, code: List[int], k: int) -> List[int]:
        '''使用滑动窗口，避免重复计算'''
        rs = [0] * len(code)
        if k >= 0:
            current = sum(code[:k])
            for i in range(0, len(code)):
                if i + k < len(code):
                    current += code[i + k] - code[i]
                else:
                    current += code[i + k - len(code)] - code[i]
                rs[i] = current
        else:
            current = sum(code[k:])
            for i in range(len(code)):
                current += code[i] - code[i + k]
                if i + 1 >= len(code):
                    rs[i + 1 - len(code)] = current
                else:
                    rs[i+1] = current
        return rs


if __name__ == '__main__':
    code = [2,4,9,3]
    k = -2
    sol = Solution()
    sol.optimalSolution(code, k)
