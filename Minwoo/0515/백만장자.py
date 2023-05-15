T = int(input())
for c in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    # 입력받은 가격들은 split() 함수를 사용하여 공백을 기준으로 분리한 후, map() 함수를 통해 정수형으로 변환하여 size 리스트에 저장
    idx = len(price) - 1
    benefit = 0

    while idx > 0:
        # 모든 가격을 검사할 때까지 반복(가장 최근의 가격은 이익을 계산할 수 없기 때문에 검사하지 않음
        for i in range(idx - 1, -1, -1):
            # idx 변수의 바로 이전 날짜부터 첫 번째 날짜까지 역순으로 for 루프를 실행
            if price[idx] > price[i]:
                benefit += price[idx] - price[i]
            else:
                idx = i
                break
        else:
            break

    print("#{} {}".format(c, benefit))


