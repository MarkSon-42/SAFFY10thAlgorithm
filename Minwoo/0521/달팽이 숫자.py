T = int(input())
for t in range(T):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]  # N x N 크기의 0으로 채워진 행렬 생성
    num = 1  # 달팽이에 채워질 숫자

    # 달팽이 채우기
    row_start = 0
    row_end = N - 1
    col_start = 0
    col_end = N - 1

    while num <= N * N:
        # 위쪽 행
        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1

        # 오른쪽 열
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # 아래쪽 행
        for j in range(col_end, col_start - 1, -1):
            matrix[row_end][j] = num
            num += 1
        row_end -= 1

        # 왼쪽 열
        for i in range(row_end, row_start - 1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1

    print("#{}".format(t+1))
    # 달팽이 출력
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()
