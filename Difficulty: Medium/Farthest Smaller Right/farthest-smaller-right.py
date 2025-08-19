class Solution:
    def farMin(self, arr):
        n = len(arr)
        ans = [-1] * n

        # Step 1: Precompute suffix minimums
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i+1])

        # Step 2: For each i, binary search in suffix_min
        for i in range(n-1):
            low, high = i+1, n-1
            pos = -1
            while low <= high:
                mid = (low + high) // 2
                if suffix_min[mid] < arr[i]:
                    pos = mid   # valid candidate
                    low = mid + 1  # try farther right
                else:
                    high = mid - 1
            ans[i] = pos

        return ans