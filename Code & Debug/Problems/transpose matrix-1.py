matrix= [
    [1,2,3],
    [4,5,6]
]

rows= len(matrix)
cols= len(matrix[0])

result= [[0]*rows for _ in range(cols)]

for i in range(0, rows):
    for j in range(0, cols):
        result[j][i]= matrix[i][j]


print(result)