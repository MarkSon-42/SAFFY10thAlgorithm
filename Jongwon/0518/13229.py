# 13229. 일요일

T = int(input())
days = {"MON" : 1, "TUE" : 2 , "WED" : 3 , "THU" : 4 , "FRI" : 5 , "SAT" : 6 , "SUN" : 7 } # 요일 별로 숫자 딕셔너리에 저장

for test_case in range(1, T+1):
    day = input()
    ans = days["SUN"] - days[day]
    if day == "SUN": # 일요일이면 7 반환
        ans = 7

    print("#{} {}".format(test_case, ans))