if __name__ == '__main__':

    def get_sum(matrix, row, col):
        sum = 0
        sum += matrix[row][col]
        sum += matrix[row-1][col-1]
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]
        return sum


    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63
    summs = []
    for i in range(1, 5):
        for j in range(1,5):
            summs.append(get_sum(arr, i, j))
             
    print(max(summs))

    