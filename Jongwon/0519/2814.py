def dfs(current, visited): # 현재 위치, 방문한 곳
    global ans
    ans = max(ans, len(visited)) # ans와 방문한 곳 수 중에서 최대값 반환

    for node in neighbor[current]: # 현재 위치와 연결된 이웃 노드들을 하나씩 연결
        if node not in visited: # 방문 안한 노드가 있으면
            dfs(node, visited+[node]) # 방문 처리



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    neighbor = [[] for _ in range(N+1)] # 이웃 노드들을 빈배열로 만들어서 구현
    for _ in range(M):
        start, end = map(int, input().split()) # 시작 노드와 끝 노드
        neighbor[start].append(end)
        neighbor[end].append(start)
        # [[], [2], [1], []]
        # [[], [2], [1, 3], [2]]

    ans = 0

    for start in range(1, N+1):
        dfs(start, [start]) # 시작하는 위치, 방문한 곳 배열

    print("#{} {}".format(test_case, ans))