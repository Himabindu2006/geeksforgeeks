class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(col) for col in zip(*mat)]
        target_sum = max(max(row_sum), max(col_sum))
        total_sum = sum(row_sum)
        return (target_sum * n) - total_sum