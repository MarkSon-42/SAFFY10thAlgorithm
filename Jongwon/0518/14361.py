T = int(input())

for test_case in range(1, T+1):
    N = input()
    nums = sorted(list(N))
    res = False
    k = 2
    
    while True:
        
        num = int(N) * k
        
        if len(str(num)) > len(N):
            break
        if sorted(list(str(num))) == nums:
            res = True
            break
        k += 1
        
    if res:
        ans = "possible"
    else:
        ans = "impossible"
     
    print("#{} {}".format(test_case, ans))