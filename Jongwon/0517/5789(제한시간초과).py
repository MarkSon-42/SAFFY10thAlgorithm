# 5789

T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    zero_arr = [0 for _ in range(N)]
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            zero_arr[j] = i+1
    
    ans = ' '.join(map(str, zero_arr))

    print("#{} {}".format(test_case, ans))