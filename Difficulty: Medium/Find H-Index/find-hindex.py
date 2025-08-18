class Solution:
    def hIndex(self, citations):
        # Sort in descending order
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations, 1):  # i starts from 1
            if c >= i:
                h = i
            else:
                break
        return h