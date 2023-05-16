# 제일 어려워.

def swap_max(num, swaps, cache):
    # 이미 계산된 경우 캐시에서 결과를 반환
    if (num, swaps) in cache:
        return cache[(num, swaps)]

    # 교환 횟수가 없는 경우 현재 숫자를 반환
    if swaps == 0:
        return num

    # 숫자를 문자열로 변환
    num_str = str(num)

    max_num = num
    # 모든 가능한 교환을 시도
    for i in range(len(num_str)):
        for j in range(i + 1, len(num_str)):
            # i, j 위치의 숫자를 교환
            swapped = num_str[:i] + num_str[j] + num_str[i + 1:j] + num_str[i] + num_str[j + 1:]
            # 교환 후 재귀적으로 함수를 호출
            swapped_max = swap_max(int(swapped), swaps - 1, cache)
            # 최대 값 업데이트
            if swapped_max > max_num:
                max_num = swapped_max

    # 결과를 캐시에 저장
    cache[(num, swaps)] = max_num
    return max_num


def solve(test_cases):
    results = []
    for i, (num, swaps) in enumerate(test_cases):
        cache = {}
        result = swap_max(num, swaps, cache)
        results.append(f"#{i + 1} {result}")
    return results

# by gpt (failed : 여전히 통과하지 않는 코드. 아이디어만 참고.)