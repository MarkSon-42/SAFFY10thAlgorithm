T = int(input())
for c in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    # 입력받은 가격들은 split() 함수를 사용하여 공백을 기준으로 분리한 후, map() 함수를 통해 정수형으로 변환하여 size 리스트에 저장
    idx = len(price) - 1
    # 리스트 인덱스는 0부터 시작하니까 len(price) - 1
    benefit = 0

    while idx > 0:
        # 모든 가격을 검사할 때까지 반복(가장 최근의 가격은 이익을 계산할 수 없기 때문에 검사하지 않음)
        for i in range(idx - 1, -1, -1):
            # idx 변수의 바로 이전 날짜부터 첫 번째 날짜까지 역순으로 for 루프를 실행
            # range(a, b, c)
            # a : sequence 시작 >>  idx - 1 부터 시작한다는 말
            # b : sequence 끝 >>  -1 ?? >> 인덱스가 0에 도달할 때 까지 루프. 0까지 포함하고 -1은 포함 안함.
            # c : sequence 단계 값 >> 시퀀스의 연속 값 사이의 증가 또는 감소를 결정
            #     각 반복에서 '1'씩 감소(-)하여 시작 값에서 중지 값으로 이동함.
            if price[idx] > price[i]:
                benefit += price[idx] - price[i]
            else:
                idx = i
                break
        else:
            break

    print("#{} {}".format(c, benefit))


