# https://angelplayer.tistory.com/325

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 선의 개수

    power_pipe = []
    count = 0

    for n in range(N):
        ai, bi = map(int, input().split())

        # process
        for ppa, ppb in power_pipe:
            if ai > ppa and bi < ppb:  # a 전봇대에서 기존의 전선보다 새로 들어온 전선의 높이가 높은 경우
                count += 1
            elif ai < ppa and bi > ppb:
                count += 1

        power_pipe.append([ai, bi])

    print(f'#{test_case} {count}')