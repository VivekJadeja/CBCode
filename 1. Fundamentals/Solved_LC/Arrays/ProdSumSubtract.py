class Solution:
    # Subtract the product and sum of a given integer
    # O(n) runtime and O(1) SC
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        for i in str(n):
            prod *= int(i)
            sum += int(i)
        return prod - sum