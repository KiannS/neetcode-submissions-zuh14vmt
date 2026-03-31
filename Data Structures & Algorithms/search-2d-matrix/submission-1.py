class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(target: int, arr: List[int]) -> bool:
            l = 0
            r = len(arr) - 1

            while (l <= r):
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
            return False

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if target < matrix[i][0]:
                continue
            if target > matrix[i][col - 1]:
                continue
            else:
                return True if binarySearch(target, matrix[i]) else False
        return False





        