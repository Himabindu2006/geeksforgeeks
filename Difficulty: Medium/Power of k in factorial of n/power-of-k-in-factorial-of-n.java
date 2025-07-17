import java.util.*;
class Solution {
    public int maxKPower(int n, int k) {
        Map<Integer, Integer> primeFactors = getPrimeFactors(k);
        int result = Integer.MAX_VALUE;

        for (Map.Entry<Integer, Integer> entry : primeFactors.entrySet()) {
            int prime = entry.getKey();
            int exponentInK = entry.getValue();
            int countInFactorial = countPrimeInFactorial(n, prime);
            result = Math.min(result, countInFactorial / exponentInK);
        }

        return result;
    }

    // Count how many times a prime p appears in n!
    private int countPrimeInFactorial(int n, int p) {
        int count = 0;
        while (n > 0) {
            n /= p;
            count += n;
        }
        return count;
    }

    // Prime factorization of k
    private Map<Integer, Integer> getPrimeFactors(int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 2; i * i <= k; i++) {
            while (k % i == 0) {
                map.put(i, map.getOrDefault(i, 0) + 1);
                k /= i;
            }
        }
        if (k > 1) {
            map.put(k, map.getOrDefault(k, 0) + 1);
        }
        return map;
    }
}