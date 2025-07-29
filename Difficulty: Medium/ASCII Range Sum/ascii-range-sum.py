class Solution:
    def asciirange(self, s):
        result = []
        for ch in set(s):  # Check each unique character
            first = s.find(ch)
            last = s.rfind(ch)
            if first != last:
                total = sum(ord(c) for c in s[first + 1:last])
                if total > 0:
                    result.append(total)
        return result