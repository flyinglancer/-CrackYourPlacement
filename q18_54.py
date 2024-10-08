class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result 
        top,bottom, left, right = 0,len(matrix),0,len(matrix[0])

        while left<right and top <bottom:
            for i in range (left,right):
                result.append(matrix[top][i])
            top += 1
            for i in range (top,bottom):
                result.append(matrix[i][right-1])
            right -= 1
            if not (left<right and top <bottom):
                break
            for i in range (right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range (bottom-1,top,-1):
                result.append(matrix[i][left])
            left +=1
        
        return result 
