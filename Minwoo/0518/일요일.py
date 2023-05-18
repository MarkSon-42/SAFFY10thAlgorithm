# 문제 선정 실패...

T = int(input())
for i in range(T):
    answer = 0
    day = input()
    if day[:2] == 'SU':
        answer = 7
    if day[:2] == 'MO':
        answer = 6
    if day[:2] == 'TU':
        answer = 5
    if day[:2] == 'WE':
        answer = 4
    if day[:2] == 'TH':
        answer = 3
    if day[:2] == 'FR':
        answer = 2
    if day[:2] == 'SA':
        answer = 1
    print("#{} {}".format(i+1, answer))