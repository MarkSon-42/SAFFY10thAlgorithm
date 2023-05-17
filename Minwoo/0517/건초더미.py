# 원래 크기의 건초더미가 되게끔 건초를 수정하는데
# +, - 연산한 값들을 모두 더해버리면 된다.

T = int(input())
for i in range(T):
    N = int(input())
    green = []
    for _ in range(N):
        size = int(input())
        green.append(size)
    # 모든 건초 더미의 크기의 합
    total_size = sum(green)
    # 모든 건초 더미의 평균 크기 :  전체 크기를 건초 더미의 수로 나눔
    average = total_size // N
    # 차이의 합계 = 건초 이동 최소 횟수
    moves = 0
    for g in green:
        if g > average:
            moves += g - average

    print(f'#{i+1} {moves}')