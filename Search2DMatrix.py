class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or target is None:
            return False
        
        r = len(matrix)
        c = len(matrix[0])
        start, end  = 0, r * c - 1
        while start <= end:
            mid = start + (end - start) / 2
            num = matrix[mid / c][mid % c]
            print "mid[" , mid / c , "][" , mid % c , "] = " , num
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
        

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    print Solution().searchMatrix(matrix, target)
        