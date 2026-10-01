class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) ==0 or len(matrix[0]) == 0:
            return False
        i_row = 0
        j_row = len(matrix) - 1

        while i_row <= j_row:
            mid = (i_row + j_row)//2
            mid_val =matrix[mid][0]
            if mid_val == target:
                return True
            elif mid_val < target:
                i_row = mid +1
            else:
                j_row = mid -1
        
        find_in = matrix[j_row]
        print(find_in)
        i = 0
        j = len(find_in) -1
        while i <= j:
            mid = (i +j)//2
            mid_val = find_in[mid]
            print('')
            print(mid)
            print(mid_val)
            if mid_val == target:
                return True
            elif mid_val < target:
                i = mid +1
            else:
                j = mid -1
        
        return False





        