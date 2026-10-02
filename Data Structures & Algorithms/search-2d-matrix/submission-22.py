class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top = 0 
        bottom = rows -1 

        while top <= bottom: 
            corr_row = (top+bottom)//2 

            if target > matrix[corr_row][-1]: 
                top = corr_row +1 
            elif target < matrix[corr_row][0]: 
                bottom = corr_row-1 
            else: 
                break 
            
        if not (top<=bottom): 
            return False 
        
        l = 0
        r = cols -1 

        while l <= r: 
            m = (l+r)//2
            if target > matrix[corr_row][m]: 
                l = m+1 
            elif target < matrix[corr_row][m]: 
                r = m -1 
            else: 
                return True 
        return False


    


        