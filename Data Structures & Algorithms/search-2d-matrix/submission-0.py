class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binarySearch(start: int, end: int, arr: List[int]) -> bool:
            if start > end:
                return False

            mid = (start + end) // 2
            if arr[mid] == target:
                return True

            l = binarySearch(start, mid - 1, arr)
            r = binarySearch(mid + 1, end, arr)
            return l or r
        
        def binSearchRow(start: int, end: int) -> int:
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                return mid

            l = binSearchRow(start, mid - 1)
            r = binSearchRow(mid + 1, end)
            return l if l >= 0 else r

        rowIndex = binSearchRow(0, m - 1)
        if rowIndex >= 0:
            return binarySearch(0, n - 1, matrix[rowIndex])
        else:
            return False