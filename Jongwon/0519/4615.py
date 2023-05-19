# 1
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)] # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    m = N//2 # 중앙에 놓고 시작한다고 해서 중앙 좌표
    arr[m][m] = arr[m+1][m+1] = 2 # 중앙에 놓는 백 돌
    arr[m][m+1] = arr[m+1][m] = 1 # 중앙에 놓는 흑 돌
    # 3
    for _ in range(M): # 초기 돌 셋팅
        si, sj, d = map(int, input().split()) # 시작 i,j, 돌 색깔
        arr[si][sj] = d
        for di,dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)): # 8방향 리스트(상왼, 상중간, 상오른, 하왼, 하중간, 하오른, 좌, 우)
            r = []
            for mul in range(1, N): # 1~ n-1 까지 뻗어나가는 거리(8방향)
                ni,nj = si+di*mul, sj+dj*mul # 다음 좌표계산
                if 1<=ni<=N and 1<=nj<=N: # 범위 내
                    if arr[ni][nj]==0: # 빈칸이면
                        break # 종료
                    elif arr[ni][nj]==d: # 같은 돌이면
                        while r: # 뒤집을 후보 배열에 좌표가 있다면
                            ti,tj = r.pop() # 배열에서 꺼낸 좌표를 뒤집을 좌표로 설정하고
                            arr[ti][tj]=d # 뒤집기
                        break
                    else: # 다른 돌이면 뒤집을 예정인 배열에 추가
                        r.append((ni,nj))
                else: # 범위 밖이면 종료
                    break
    # 2
    bcnt = wcnt = 0 # 흑돌, 백돌 초기화
    for lst in arr:
        bcnt += lst.count(1) # 흑돌 개수
        wcnt += lst.count(2) # 백돌 개수
 
    print(f'#{test_case} {bcnt} {wcnt}')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    table = [[0] * (N+1) for _ in range(N+1)] # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    m = N // 2 # 중간 위치를 위해 중간 값
    # 1. 초기 돌 놓기
    table[m][m] = table[m+1][m+1] = 2 # 백돌 초기 돌 위치
    table[m][m+1] = table[m+1][m] = 1 # 흑 돌 초기 돌 위치

    # 2. 입력 받은 좌표에 돌 놓기 (8방향 뻗어나가면서 처리)
    for _ in range(M):
        start_i, start_j, color = map(int, input().split())
        table[start_i][start_j] = color
        for direction_i, direction_j in ((-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)): # 돌의 8가지 갈 수 있는 방향 선언
            change = [] # 색깔이 바뀔 예정인 돌의 좌표를 받는 리스트
            for distance in range(1, N):
                next_i, next_j = start_i + direction_i * distance,  start_j + direction_j * distance # 다음 좌표는 시작 좌표에 방향 좌표와 거리를 곱한 만큼을 더해줌
                # 3. 2번을 범위 내와 밖으로 나눠서 처리
                if 1 <= next_i <= N and 1 <= next_j <= N: # 테이블 내일때
                    # 5. 범위 내는 (1) 빈칸이 0이면 끝내고 다음방향 (2) 놓은 돌과 다른 돌이면 뒤집을 후보에 추가(reverse 배열) 하고 다음 방향 (3) 같은 돌이면 뒤집을 후보들 다 뒤집고 다음 방향
                    if table[next_i][next_j] == 0: # 다음 좌표가 빈칸이면 종료
                        break 
                    elif table[next_i][next_j] == color: # 다음 좌표가 같은 색깔이면
                        while change: # 색을 바꿀 좌표가 있으면
                            ci, cj = change.pop() # 배열에서 뺀 좌표를 
                            table[ci][cj] = color # 같은 색깔로 바꿔준다
                        break # 종료

                    else: # 색깔이 다르면
                        change.append((next_i, next_j)) # 색을 바꿀 예정 목록에 좌표를 넣어준다 
                # 4. 범위 밖은 아무일도 일어나지 않고 return
                else: # 테이블 범위 밖이면
                    break # 종료

    black_cnt = 0
    white_cnt = 0
    for stone in table: # 각 색깔의 돌 개수 세서 반환
        black_cnt += stone.count(1)
        white_cnt += stone.count(2)

    print("#{} {} {}".format(test_case, black_cnt, white_cnt))