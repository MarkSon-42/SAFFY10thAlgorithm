# 준환이의 운동 관리
# L분이상 U분이하 운동
# 이번주 X만큼 운동함

T=int(input())
for i in range(1,T+1):
    l,u,x=list(map(int,input().split()))

    if x>u:
        print(f'#{i} {-1}')
    elif x<l:
        print(f'#{i} {l-x}')
    else:
        print(f'#{i} {0}')

