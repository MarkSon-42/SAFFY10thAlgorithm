# 1860. 진기의 최고급 붕어빵

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort() # M으로 나누기 위해서 정렬

    result = "Possible"
    
    for i in range(N):
        carp = (arrive[i] // M) * K - (i+1) # 도착한 시간까지 만들어진 붕어빵의 개수: (x // M) * K - 이미 사간 개수
        if carp < 0:
            result = "Impossible"
            break

    print("#{} {}".format(test_case, result))