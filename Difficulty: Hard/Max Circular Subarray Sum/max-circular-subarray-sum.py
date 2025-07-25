class Solution:
    def maxCircularSum(self, arr):
        total_sum = 0
        max_kadane = float('-inf')
        min_kadane = float('inf')
        current_max = 0
        current_min = 0

        for num in arr:
            total_sum += num

            # Kadane for max subarray (non-wrapping)
            current_max = max(num, current_max + num)
            max_kadane = max(max_kadane, current_max)

            # Kadane for min subarray (to calculate wrapping)
            current_min = min(num, current_min + num)
            min_kadane = min(min_kadane, current_min)

        # If all numbers are negative, max wrap would be 0, which is invalid
        if total_sum == min_kadane:
            return max_kadane
        else:
            return max(max_kadane, total_sum - min_kadane)