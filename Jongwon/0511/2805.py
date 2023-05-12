# 2805 농작물 수확하기
# i 값에 따른 j값의 변화의 규칙성을 찾아서 해결

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
 
    M = N//2 # 중간값(기준)
    ans = 0
    for i in range(N):
        if i<=M:
            for j in range(M-i, M+i+1): # 중간값 보다 작을때의 i값의 따라 j의 규칙성 찾은 후 식으로 범위로 설정
                ans += arr[i][j]
        else:
            for j in range(i-M, N-(i-M)): # 중간값 보다 클 때의 i값에 따라 j의 규칙성을 찾은 후 식으로 범위로 설정
                ans += arr[i][j]
 
    print("#{} {}".format(test_case, ans))