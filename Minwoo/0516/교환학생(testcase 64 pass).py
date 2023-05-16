# 끔찍한 하드코딩 입니다.

TC = int(input())
for t in range(1, TC + 1):
    n = int(input())
    cnt, i, j, k, loop_cnt = 0, 0, 0, 0, 0
    lectures = list(map(int, input().split()))
    sum_lect = sum(lectures)
    if n == sum_lect:
        while n > 0:
            if lectures[i] == 1:
                n -= 1
                i += 1
            loop_cnt += 1

    elif n != 1 and sum_lect == 1:
        while n > 1:
            loop_cnt = ((n // sum_lect) - 1) * 7
            n -= 1
            if n == 1:
                for k in range(7):
                    if lectures[k] == 1:
                        n -= 1
                        break
                    loop_cnt += 1


    else:
        loop_cnt = (n // sum_lect) * 7
        left_cnt = n % sum_lect
        while left_cnt > 0:
            if lectures[j] == 1:
                left_cnt -= 1
                loop_cnt += 1
            j += 1

    print("#{} {}".format(t, loop_cnt))