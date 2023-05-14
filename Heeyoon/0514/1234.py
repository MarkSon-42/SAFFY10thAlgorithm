# 비밀번호


for i in range(1,11):
    n, pswd = input().split()
    a=''
    for j in pswd:
        if a and j==a[-1]:
            a=a[:-1]
        else:
            a+=j
    print(f'#{i} {a}')