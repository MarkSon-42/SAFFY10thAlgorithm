T = int(input())
for tc in range(1, T + 1):
    not_submited = []
    N, K = map(int, input().split())
    submitted = list(map(int, (input().split())))
    students = list(range(1, N+1))
    for i in range(N):
        if students[i] not in submitted:
            not_submitted.append(students[i])

    not_submitted = ' '.join(map(str, not_submitted))
    print("#{} {}".format(tc, not_submitted))

# 지나치게 어렵게 푼 것 같소.
# 굳이 list()를 이렇게 남발할 필요가 없는거 같다.
# 더 좋은 풀이를 찾아보자.