# 13038 교환학생

T = int(input())
 
for test_case in range(T):
    n = int(input())
    days = list(map(int, input().split()))
    cnt_lst = []
 
    for a in range(7):
        cnt2 = 0
        b = a
        cnt1 = 0
        while cnt2 < n:
            if days[b] == 1:
                cnt2+=1
            b+=1 # 일주일 도는용
            cnt1+=1
            if b == 7: # 연속된 날짜 제거용
                b=0
    
        cnt_lst.append(cnt1) # 모든 첫 개강일을 담아두는 배열을 만들고,그 배열을 for문을 통해 돌면서, 각 첫 개강일마다의 최소 일수를 계산했다.그리고 그 최소 일수들의 최솟값
    print("#{} {}".format(test_case+1,min(cnt_lst)))

# 연속된 날짜 테스트 케이스 
# 1 0 0 0 0 0 1
# 위 테스트 케이스는 일요일(a1)과 토요일(a7)에 강의가 열리는데, 이는
# 1 1 0 0 0 0 0
# 이 일요일(a1), 월요일(a2)에 강의가 열리는 테스트 케이스와 정답이 똑같이 나와야 한다.
