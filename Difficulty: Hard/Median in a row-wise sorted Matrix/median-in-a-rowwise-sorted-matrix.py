import bisect

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])

        # Minimum element in matrix (smallest of first elements in each row)
        low = min(row[0] for row in mat)
        # Maximum element in matrix (largest of last elements in each row)
        high = max(row[-1] for row in mat)

        desired = (n * m + 1) // 2  # position of median (1-based index)

        while low < high:
            mid = (low + high) // 2

            # Count of elements <= mid
            count = 0
            for row in mat:
                # Use bisect_right to count how many elements <= mid in a row
                count += bisect.bisect_right(row, mid)

            if count < desired:
                low = mid + 1
            else:
                high = mid

        return low