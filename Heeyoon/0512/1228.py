# 암호문
# insert까지는 어찌저찌 했는데
# 마지막에 insert랑 join 을 제대로 못해서 실패

# I(삽입) x,y,s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
# s는 덧붙일 숫자들이다.
# ex) I 3 2 123152 487651

for t in range(10):
    # 원본 암호문의 길이
    pswd_num = int(input())
    # 원본 암호문
    pswd = list(map(int, input().split()))
    # 명령어의 개수
    word_num = int(input())
    # 명령어
    word = list(input().split())

    for i in range(len(word)):
        # i가 I에 걸리는지 체크
        if word[i] == 'I':
            # I에 걸렸으면 그 다음에 오는 숫자를 x, 그 다음에 오는 숫자를 y로 받음
            index = int(word[i+1])  # I 다음 x ( x의 위치 다음에 )
            nums = int(word[i+2])  # y ( y개의 숫자 삽입 )
            # y만큼 도는 동안
            for j in range(nums):
                # x+j의 위치에 nums+j+1의 숫자들을 삽입
                pswd.insert(index+j, int(word[i+2+(j+1)]))
        else:
            continue
    print('#{} {}'.format(t+1, ' '.join(map(str, pswd[:10]))))
