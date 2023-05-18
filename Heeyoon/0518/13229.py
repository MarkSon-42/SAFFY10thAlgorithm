'''
13229
오늘의 요일을 나타내는 문자열 S가 주어진다. S는 “MON”(월), “TUE”(화), “WED”(수), “THU”(목), “FRI”(금), “SAT”(토), “SUN”(일) 중 하나이다.

다음 (즉, 내일 이후의 가장 빠른) 일요일까지는 며칠 남았을까?


3
SUN
SAT
MON


#1 7
#2 1
#3 6
'''
tc = int(input())
for i in range(tc):
    s=input()
    w=7
    week=['SUN','MON','TUE','WED','THU','FRI','SAT']
    if s in week:
        # if s=='SUN':
        #     print(f'#{i+1} 7')
            
        print(f'#{i+1} {7-(week.index(s))}')