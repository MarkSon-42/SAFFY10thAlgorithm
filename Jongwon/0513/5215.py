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

    # 그 중에서 가장 큰 점수 추출