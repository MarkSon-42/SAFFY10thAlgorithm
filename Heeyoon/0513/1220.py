# magnetic
# 빨간색1, 파란색2


T=10
for i in range(1,T+1):
    num=int(input())
    arr=[list(map(int,input().split())) for _ in range(num)]

    cnt=0

    arr_t = list(zip(*arr)) # 전치행렬 만들기

    for lst in arr_t:
        prev=0
        for n in lst:
            if n:
                if n==2 and prev==1: # 교착상태
                    cnt+=1
                prev=n
    print(f'#{i} {cnt}')