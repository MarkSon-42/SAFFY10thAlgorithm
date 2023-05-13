#진기의 붕어빵
T=int(input())


for i in range(1,T+1):
    n,m,k=map(int,input().split())
    # arr1,arr2=map(int,input().split())
    
    arrTime=list(map(int,input().split()))  
    arrTime.sort()

    result='Possible'

    for j in range(n):
        # if m//k==arrTime[j] or m//k==0 or m//k<0:
        # bb = (arrTime[j])*(k//m)
        bb = (arrTime[j]//m)*k-(j+1)
        if bb<0:
            result='Impossible'
            break
        
    print(f'#{i} {result}')
 

