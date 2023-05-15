T = int(input()) # 테스트 케이서 입력

for i in range(1, T + 1):
    # range()의 범위   1 부터 T까지 반복
    cnt = 0
    # 변경 횟수를 카운트 하는 변수
    m = list(input())
    # 각 테스트 케이스에 대한 문자열 m을 입력받아 리스트로 변환
    origin = len(m) * ['0']
    # 원래 문자열과 동일한 길이의 '0'으로 채워진 리스트 작성.
    for j in range(len(m)):
        # m길이 만큼 반복
        if m[j] != origin[j]:
            # 만약 m의 j번째 요소와 origin의 j번째 요소가 다르다면
            for k in range(j, len(m)):
                # j부터 m의 길이까지 반복
                origin[k] = m[j]
                # origin의 k번째 요소를 m의 j번째 요소로 변경
            cnt += 1

    print("#{} {}".format(i, cnt))