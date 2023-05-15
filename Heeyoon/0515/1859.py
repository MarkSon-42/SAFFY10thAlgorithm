# 백만 장자 프로젝트
T=int(input())
for t in range(1,T+1):
    days=int(input())
    arr=list(map(int,input().split()))
    # 마지막 날의 시세
    last=arr[-1]
    cnt=0
    # 길이부터 0까지 -1씩 빼면서 뒤에서부터 카운트
    for i in range(len(arr)-1,-1,-1): 
        if last>arr[i]: # 마지막 날 시세가 현재 시세보다 크면
            cnt+=last-arr[i] # 마지막 날 시세 - 오늘 시세
        else: # 마지막 날 시세가 현재 시세보다 작거나 같으면
            last= arr[i] # 마지막 날 시세 == 현재 시세
    print(f'#{t} {cnt}')


