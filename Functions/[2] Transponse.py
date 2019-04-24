# Transpose a matrix

def transpose(matrix):
   b = matrix
   res = []
   n = len(matrix)
   m = len(matrix[0])
   for i in range(m):
       tmp = []
       for j in range(n):
           tmp = tmp + [matrix[j][i]]
       res = res + [tmp]
   matrix = res
   return res
   
matrix = [[1,2,3],[3,4,5]]
print(transpose(matrix))
for line in matrix:
   print(*line)


