# 5215. 햄버거 다이어트

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    
    ingredient = []
    for _ in range(N):
        T, K = map(int, input().split())
        ingredient.append((T, K))

    combination = [[] for _ in range(N)] # 점수와 칼로리 조합 

    # L을 넘지 않은 모든 조합을 combination에 저장
    for i in range(N):
        combination[i].append(ingredient[i])
        for j in range(0, i):
            for k in combination[j]:
                T, K = k
                if K + ingredient[i][1] <= L:
                    combination[i].append((T + ingredient[i][0], K + ingredient[i][1]))


    # 그 중에서 가장 큰 점수 추출
    max_score = 0
    for i in range(N):
        for j in combination[i]:
            T, K = j
            if T > max_score:
                max_score = T
    
    print("#{} {}".format(test_case, max_score))