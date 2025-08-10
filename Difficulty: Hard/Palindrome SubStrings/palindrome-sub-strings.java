class Solution {
    public int countPS(String s) {
        int count = 0;
        int n = s.length();

        for (int center = 0; center < n; center++) {
            count += expandFromCenter(s, center, center);     // odd-length palindromes
            count += expandFromCenter(s, center, center + 1); // even-length palindromes
        }

        return count;
    }

    private int expandFromCenter(String s, int left, int right) {
        int count = 0;

        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            if (right - left + 1 >= 2) {
                count++;
            }
            left--;
            right++;
        }

        return count;
    }
}