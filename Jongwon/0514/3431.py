# 3431 준환이의 운동관리

T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    
    if L <= X <= U: # 범위 내이면 0반환
        ans = 0
    elif X > U: # 최대 시간 보다 크면 -1 반환
        ans = -1
    elif L > X: # 최소 시간 보다 작으면 최소 시간 - 이번주에 운동한 시간 반환
        ans = L - X
        
    print("#{} {}".format(test_case, ans))