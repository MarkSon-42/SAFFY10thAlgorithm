t = 10
for test_case in range(1, t + 1):  # 테스트 케이스의 개수 t를 입력받아 for loop으로 반복한다.
    dmp_cnt = int(input())  # 덤프 횟수를 입력받는다.
    numbers = list(map(int, input().split()))  # 박스에 담긴 높이를 입력받아 리스트로 저장한다.


    for i in range(dmp_cnt):  # 덤프 횟수만큼 for loop을 반복한다.
        max_num = max(numbers)  # 박스 중 가장 높은 박스를 찾는다.
        min_num = min(numbers)  # 박스 중 가장 낮은 박스를 찾는다.
        index_max_num = numbers.index(max_num)  # 가장 높은 박스의 인덱스를 찾는다.
        index_min_num = numbers.index(min_num)  # 가장 낮은 박스의 인덱스를 찾는다.
        numbers[index_max_num] -= 1  # 가장 높은 박스에서 높이를 1만큼 내린다.
        numbers[index_min_num] += 1  # 가장 낮은 박스에서 높이를 1만큼 높인다.

    print('#{} {}'.format(test_case, max(numbers) - min(numbers)))  # 결과값을 출력한다. 최고점과 최저점의 차이를 출력한다.
