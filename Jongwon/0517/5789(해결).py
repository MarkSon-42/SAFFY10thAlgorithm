# 5789 
# 1~ q+1로 했는데 시간초과나서 q로 바꾸고 밑에 i+1로 바꿔서 해결

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