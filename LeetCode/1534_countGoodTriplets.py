from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        sum = 0
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        sum+=1
        return sum


if __name__ == '__main__':
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    s = Solution()
    print(s.countGoodTriplets(arr, a, b, c))
