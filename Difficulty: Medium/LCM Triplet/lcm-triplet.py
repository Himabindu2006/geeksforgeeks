import math
class Solution:
    def lcm(self, a, b):
        return a * b // math.gcd(a, b)
    def lcm_of_three(self, a, b, c):
        return self.lcm(self.lcm(a, b), c)
    def lcmTriplets(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n % 2 != 0:
            return self.lcm_of_three(n, n-1, n-2)
        else:
            if math.gcd(n, n - 3) == 1:
                return self.lcm_of_three(n, n - 1, n - 3)
            else:
                return self.lcm_of_three(n - 1, n - 2, n - 3)