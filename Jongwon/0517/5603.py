# 5603

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lays = []
    for i in range(N):
        S = int(input())
        lays.append(S)
        
    
    avg = sum(lays) // N # 평균값
    ans = 0 
    for j in range(len(lays)): # 평균값보다 작은 건초더미들을 찾아서 평균값에서 크기를 뺀 값으로 ans에 더해서 갱신하여 횟수 반환
        if lays[j] < avg:
            ans += (avg - lays[j])
    
    print("#{} {}".format(test_case, ans))