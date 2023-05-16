#민석이의 과제 체크
# 수강생들 1번부터 n번까지 , 과제 제출한 k명
# 1~n 생성, 1~k 생성
# 다음줄 k 원소 입력받
# n까지 세는데 
T=int(input())

for t in range(1,T+1):
    n,k=map(int,input().split())
    box=[]
    # for i in range(1,n+1):
    #     box.append(i)
    students=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in students:
            box.append(i)
    # print(f'#{t} {*box}')
    print('#{}'.format(t),*box)