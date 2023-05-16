# 10 포인트 사용해서 적당한 코드 하나 조회.

import math

for tc in range(1, int(input()) + 1):
    n = int(input())
    a = list(input().split())
    c = a.count('1')
    days = (math.ceil(n / c) - 1) * 7

    t = []
    for i in range(7):
        if a[i] == '1':
            t.append(i)
    m = []
    for i in range(len(t)):
        temp = days
        tj = t[(i + n % c - 1) % len(t)]
        if t[i] <= tj:
            temp += tj - t[i] + 1
        else:
            temp += 8 - t[i] + tj
        m.append(temp)

    print(f"#{tc} {min(m)}")