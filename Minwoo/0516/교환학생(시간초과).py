TC = int(input())
for t in range(1, TC + 1):
    n = int(input())
    cnt, i, loop_cnt = 0, 0, 0
    lectures = list(map(int, input().split()))
    while n - cnt != 0:
        if lectures[i] == 1:
            cnt += 1
        if i == 6:
            i = 0
        loop_cnt += 1
    print("#{} {}".format(TC, loop_cnt))

# TC = 1에 n = 2, a.. = [1 0 1 0 0 0 0] 으로
# 테스트해도 시간초과 나옴 ( ??? )