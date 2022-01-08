def check_another(matrix, mas):
    row = mas[0]
    col = mas[1]
    l = len(matrix)
    if(matrix[row][col] == 1 or matrix[row][col] == 2):
        matrix[row][col] = 2
        if(row + 1 < l):
            check_another(matrix, [row+1, col])
        if(row - 1 > 0):
            check_another(matrix, [row-1, col])
        if(col + 1 < l):
            check_another(matrix, [row, col+1])
        if(col - 1 > 0):
            check_another(matrix, [row, col-1])
    
def remuveIslands(matrix):
    # 1 -> black
    # 0 -> white 
    # remuve all black pixels, which not conected to the border  
    l = len(matrix)
    
    for i in range(1, l-1):
        if(matrix[0][i] == 1):
            check_another(matrix, [1,i])
        if(matrix[l-1][i] == 1):
            check_another(matrix, [l-2,i])
        if(matrix[i][0] == 1):
            check_another(matrix, [i,1])
        if(matrix[i][l-1] == 1):
            check_another(matrix, [i,l-2])
    
def Print(matrix):
    l = len(matrix)
    for i in range(l):
        for j in range(l):
            print(matrix[i][j], end = " ")
        print("\n")

if __name__ == '__main__':
    matrix = []
    #len
    n = int(input())
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    print("__________")
    remuveIslands(matrix)
    
    Print(matrix)
