T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N, K = map(int, input().split())  # N: 학생 수, K: 과제를 제출한 사람 수
    submitted = list(map(int, input().split()))  # 과제를 제출한 사람들의 리스트

    not_submitted = []
    for i in range(1, N+1):
        if i not in submitted:
            not_submitted.append(i)

    print(f'#{test_case}', end=' ')
    for num in not_submitted:
        print(num, end=' ')
    print()

# 내 풀이랑 거의 같은데, 반복문과 출력이 훨씬 더 간략하고 직관적이다.

# 라인 7~10 그리고 라인 12~15 참고.