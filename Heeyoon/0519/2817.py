n=int(input())


for i in range(1,n+1):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))

    allSum = sum(nums)

    sums=[]
    cnt=0
    for num in nums:
        lenSums = len(sums)
        sums.append(num)
        if num ==k:
            cnt+=1
        for s in range(lenSums):
            newSum = sums[s]+num
            if newSum<k:
                sums.append(newSum)
            elif newSum ==k:
                cnt+=1
    print(f'#{i} {cnt}')




