import math

class Solution:
    def countNumbers(self, n):
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(math.isqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        primes = []
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if is_prime(i):
                primes.append(i)

        count = 0

        # Case 1: p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2
        plen = len(primes)
        for i in range(plen):
            for j in range(i + 1, plen):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    count += 1
                else:
                    break

        return count

        