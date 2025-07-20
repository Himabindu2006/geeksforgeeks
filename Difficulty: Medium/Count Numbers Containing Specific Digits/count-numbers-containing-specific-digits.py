class Solution:
    def countValid(self, n, arr):
        # code here
        forbidden = set(arr)
        allowed = set(range(10)) - forbidden

        # Total n-digit numbers
        if n == 1:
            total = 9  # numbers from 1 to 9
            # Only 1-9 are valid one-digit numbers.
            total_without = len([d for d in allowed if 1 <= d <= 9])
        else:
            total = 9 * pow(10, n-1)  # numbers from 10^(n-1) to 10^n-1
            if not allowed:
                total_without = 0
            else:
                first_digit_opts = len(allowed) - (1 if 0 in allowed else 0)
                total_without = first_digit_opts * pow(len(allowed), n-1)
                    
        return total - total_without