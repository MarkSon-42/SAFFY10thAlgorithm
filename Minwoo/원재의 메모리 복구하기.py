# 그냥 구현.

T = int(input())

for i in range(1, T + 1):
    cnt = 0
    m = list(input())
    origin = len(m) * ['0']
    for j in range(len(m)):
        if m[j] != origin[j]:
            for k in range(j, len(m)):
                origin[k] = m[j]
            cnt += 1

    print("#{} {}".format(i, cnt))