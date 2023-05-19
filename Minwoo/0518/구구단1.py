TC = int(input())

for i in range(TC):
    gugu_list = []
    for j in range(1, 10):
        for k in range(1, 10):
            gugu_list.append(j*k)
    gugu_list = set(gugu_list) # 굳이 할 필요 없는데 그냥 해봄
    N = int(input())
    if N in gugu_list:
        answer = "Yes"
    else:
        answer = "No"
    print("#{} {}".format(i + 1, answer))
