T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    # 큰값부터 봐야하니까 내림차순으로 정렬하자.
    max_score = 0
    for j in range(K):
        max_score += score[j]
    print("#{} {}".format(i, max_score))

    # ... D3가 맞나?