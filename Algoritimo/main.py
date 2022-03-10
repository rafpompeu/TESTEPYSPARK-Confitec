A = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
B = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
n = range(len(A[0])) #numero de colunas
m = range(len(A)) #numero de linhas


product = [[0 for x in n] for y in m]
for i in m:
    for j in n:
        for k in m:
            product[i][j] += A[i][k] * B[k][j]
print(product)