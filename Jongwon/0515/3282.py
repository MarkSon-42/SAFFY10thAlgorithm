# 3282

T = int(input())
for test_case in range(1, T+1):
    n,k = map(int,input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    items = [list(map(int,input().split())) for _ in range(n)]

    for i in range(1,n+1):
        for j in range(1,k+1):
            if items[i - 1][0] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1][1] + dp[i - 1][j - items[i - 1][0]])
            else:
                dp[i][j] = dp[i - 1][j]
    print("#{} {}".format(test_case, dp[n][k]))



# 구글링(참고 코드)

# 각 아이템에 대해서 가방의 크기를 0부터 1씩 최대무게까지 늘려가며 계산.

# 가방의 크기가 해당 아이템의 무게보다 작으면 아이템을 넣지 못한다. 이전까지의 무게와 가치 적용

# 가방의 크기가 해당 아이템의 무게보다 크면 아이템을 넣을지 말지 선택한다.

# 이전까지의 무게와 가치 vs (이전까지의 무게 - 현재 아이템의 무게)의 가치 + 현재 아이템의 가치



# 입력
T = int(input())
Ns = []
for tc in range(T):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    Ns.append((N, K, items))

# 풀이
results = []

for tc in range(T):
    N, K, items = Ns[tc]
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, len(dp)):
        v, c = items[i - 1]
        for j in range(1, len(dp[i])):
            # 가방에 아이템이 들어 갈 수 있으면
            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]

    results.append(dp[-1][-1])

# 출력
for tc in range(T):
    print(f'#{tc + 1} {results[tc]}')
