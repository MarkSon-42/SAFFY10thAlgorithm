# 문제를 이해 못함

# T = int(input())
# for _ in range(T):
#     bits = input()
#     cnt = 0
#     for b in bits:
#         if b != '0':
#             bits[b:] = '1'
#             cnt += 1
#         else:
#             continue
#     print(cnt)


T = int(input())

for i in range(1, T+1):
    cnt = 0
    m = list(input())
    origin = len(m) * ['0']
    for j in range(len(m)):
        if m[j] != origin[j]:
            for k in range(j, len(m)):
                origin[k] = m[j]
            cnt += 1

    print("#{} {}".format(i, cnt))