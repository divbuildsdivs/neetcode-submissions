class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        mul = 1
        while mul*2 <= n:
            mul *= 2
        count = 0

        while n > 0:
            if n >= mul:
                count += 1
                n = n - mul
            mul = mul//2
        return count
        