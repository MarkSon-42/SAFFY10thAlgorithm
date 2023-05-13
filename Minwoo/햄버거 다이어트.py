# 다이어트 최적 조합 햄버거 찾기
def find_best_hamburger(T, test_cases):
    results = []
    # 각 테스트 케이스에 대한 결과를 저장할 리스트를 생성

    for t, (N, L, ingredients) in enumerate(test_cases, start=1):
        dp = [0] * (L + 1)
        # DP 배열을 초기화 한다.
        # 예제의 경우라면 1000 + 1 이니까 길이는 1001

        for taste, calorie in ingredients:
            # 칼로리 제한 내에서 가능한 조합을 찾아 taste 점수를 최대화
            for j in range(L, calorie - 1, -1):
                dp[j] = max(dp[j], dp[j - calorie] + taste)

        results.append(f"#{t} {dp[L]}")
        # 결과를 리스트에 추가

    return results

def main():
    T = int(input())
    test_cases = []

    # 각 테스트 케이스에 대해 입력을 받습니다.
    for _ in range(T):
        N, L = map(int, input().split())
        ingredients = [tuple(map(int, input().split())) for _ in range(N)]
        # 각 재료의 taste 점수와 칼로리를 입력
        # 리스트 컴프리헨션으로 받는데 튜플 타입으로 받음

        test_cases.append((N, L, ingredients))
        # 테스트 케이스를 리스트에 추가

    results = find_best_hamburger(T, test_cases)

    # 각 테스트 케이스의 결과 출력
    for result in results:
        print(result)
