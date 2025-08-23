class Solution:
    def is_valid(self, arr, k, max_pages):
        students = 1
        current_sum = 0
        for pages in arr:
            if pages > max_pages:
                return False  
                
            if current_sum + pages > max_pages:
                students += 1
                current_sum = pages
                if students > k:
                    return False
            else:
                current_sum += pages

        return True
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1  
        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(arr, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result