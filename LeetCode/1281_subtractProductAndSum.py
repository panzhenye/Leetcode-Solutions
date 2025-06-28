class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        multiply=1
        for i in str(n):
            sum+=int(i)
            multiply*=int(i)
        return multiply-sum

if __name__ == '__main__':
    n=4421
    sol=Solution()
    print(sol.subtractProductAndSum(n))