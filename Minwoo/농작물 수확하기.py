T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())  # 농장의 크기
    farm = []  # 농장 정보를 저장할 리스트

    # 농작물 가치 입력
    for i in range(N):
        row = list(map(int, input()))
        farm.append(row)

    max_sum = 0  # 최대 가치의 합

    # 모든 마름모를 탐색하면서 그 안에 있는 작물 가치의 합을 계산하고, 최대값을 찾는다.
    for size in range(1, N+1, 2):
        for i in range(N-size+1):  # 마름모의 시작점 i
            for j in range(N-size+1):  # 마름모의 시작점 j
                sub_sum = 0
                for x in range(size):  # 마름모의 각 위치 x, y에 대해서
                    for y in range(size):
                        # 마름모 내부에 위치하면서 중앙점으로부터의 거리가 마름모 크기의 반을 넘지 않는 경우에만 작물 가치의 합을 더한다.
                        if abs(x - size//2) + abs(y - size//2) <= size//2:
                            sub_sum += farm[i+x][j+y]
                if sub_sum > max_sum:
                    max_sum = sub_sum

    print("#{} {}".format(test_case, max_sum))  # 결과 출력