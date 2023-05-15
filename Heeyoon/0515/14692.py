# 통나무 자르기

T=int(input())

for i in range(1,T+1):
    num=int(input())
    if num%2==1:
        print(f'#{i} Bob')
    else:
        print(f'#{i} Alice')