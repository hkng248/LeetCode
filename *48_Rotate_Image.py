#What made this problem difficult was the referencing of rows as you modify the matrix 
#You have to swap two values concurrently. You cannot swap values one at a time

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(n):
            matrix[i].reverse()
                
        # This code  works if you have to rotate the matrix and use another matrix 
        # Research python referencing! 
        # matrixCopy = []
        # for i in range(0, len(matrix[0])):
        #     matrixCopy.append( [0]*len(matrix[0]))       
        # lines = []
        # for i in matrix:
        #     c = i 
        #     lines.append(c) 
        # column = len(matrix) - 1 
        # for line in lines:
        #     c = 0 
        #     for j in line:
        #         matrixCopy[c][column] = j  # this is where the test case will fail (incorrect referencing / modifications) 
        #         c += 1 
        #     column -= 1
        # print(matrixCopy)

            
        