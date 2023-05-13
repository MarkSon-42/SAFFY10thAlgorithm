T = int(input())

for i in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 사람수, 시간(초), 붕어빵 생산 가능 개수 입력받기.
    times = list(map(int, input().split()))
    # 시간을 리스트 형태로 받아준다. (이후에 정렬까지)
    answer = ''
    times.sort()
    for j in range(N):
        if (times[j] // M) * K < j + 1:
            answer = "Impossible"
            break
        else:
            answer = "Possible"
    print("#", i, " ", answer, sep='')