class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftArray = 0
        rightArray = len(matrix) - 1

        while leftArray <= rightArray:
            midArray = (leftArray + rightArray) // 2

            left = 0
            right = len(matrix[midArray]) - 1

            if target < matrix[midArray][left]:
                rightArray = midArray - 1
            elif target > matrix[midArray][right]:
                leftArray = midArray + 1
            else:
                while left <= right:
                    mid = (left + right) // 2
                    if target < matrix[midArray][mid]:
                        right = mid - 1
                    elif target > matrix[midArray][mid]:
                        left = mid + 1
                    else:
                        return True

                return False
        
        return False


                
        