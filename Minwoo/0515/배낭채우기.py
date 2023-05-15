def knapsack(N, K, volumes, values):
    # dp 초기화 : 이건... 거의 공식이자 패턴
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            # 현재 물건을 선택하지 않는 경우
            dp[i][j] = dp[i-1][j]

            # 현재 물건을 선택하는 경우
            if volumes[i-1] <= j:
                dp[i][j] = max(dp[i][j], values[i-1] + dp[i-1][j - volumes[i-1]])

    return dp[N][K]

T = int(input())

for t in range(T):
    # 물건의 개수 N과 가방의 용량 K를 입력받습니다.
    N, K = map(int, input().split())

    volumes = []
    values = []
    for _ in range(N):
        volume, value = map(int, input().split())
        volumes.append(volume)
        values.append(value)

    # 최대 가치를 계산합니다.
    max_value = knapsack(N, K, volumes, values)

    # 결과를 출력합니다.
    print(f"#{t} {max_value}")
