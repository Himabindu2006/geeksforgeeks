class Solution:
    def countRevPairs(self, arr):
        # Code here 
        import bisect
        cnt = 0
        sorted_arr = []
        for e in arr:
            searched = e*2
            i = bisect.bisect_right(sorted_arr, searched)
            cnt += len(sorted_arr)-i
            bisect.insort_left(sorted_arr, e)
        return cnt