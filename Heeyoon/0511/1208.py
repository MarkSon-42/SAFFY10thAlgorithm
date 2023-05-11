# [S/W 문제해결 기본] 1일차 - Flatten 


T=int(input())

'''
리스트에서 정렬시켜서 제일 큰 원소와 제일 작은 원소 찾기
max에서 -1, min에 +1
@ 
마지막에 max - min 해서 리턴
'''

'''
for i in range(1,11):
    num=int(input())
    a=list(map(int,input().split()))

    for _ in range(num):
        a.sort()
        a[0]+=1
        a[-1]-=1
        
        max_d = max(a)
        min_d = min(a)
        
        # 최대값과 최소값을 찾아놓고
        # 값의 위치를 찾아야 줄이거나 늘일수 있기 때문에
        # 그것들의 인덱스 찾기
        
        max_idx = a.index(max_d)
        min_idx = a.index(min_d)

        a[max_idx]-=1
        a[min_idx]+=1
        

    print(f'#{i} {max(a)-min(a)}')


# print(f'#{j} {sum}')
'''

# [S/W 문제해결 기본] 1일차 - Flatten 

for i in range(1,11):
    num=int(input())
    a=list(map(int,input().split()))

    for _ in range(num):
        a.sort()
        a[0]+=1
        a[-1]-=1

    print(f'#{i} {max(a)-min(a)}')




