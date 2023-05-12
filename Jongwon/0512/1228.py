# 1228 암호문1

tc = 10

for test_case in range(tc):

    first = int(input()) # 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)

    second = list(map(int, input().split())) # 두 번째 줄 : 원본 암호문

    third = int(input()) # 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)

    fourth = list(input().split()) # 네 번째 줄 : 명령어

    for i in range(len(fourth)):
        if fourth[i] == 'I': # I(삽입) 명령어
            x = int(fourth[i+1]) # x(위치)
            y = int(fourth[i+2]) # y(숫자 개수)
            for j in range(y):
                fourth.insert(x+j,int(fourth[i+2+(j+1)])) # 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
        else:
            continue
    print('#{} {}'.format(test_case+1,' '.join(map(str,fourth[:10])))) # 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라