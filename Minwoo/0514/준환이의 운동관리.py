T = int(input())
for tc in range(1, T + 1):
    answer = 0
    L, U, X = map(int, input().split())
    if L - X > 0:
        answer = L - X
    if L - X <= 0 and U > X:
        pass
    if X > U:
        answer = -1

    print("#{} {}".format(tc, answer))
