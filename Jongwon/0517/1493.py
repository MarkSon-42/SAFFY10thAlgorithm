# 1493

# 로직 자체는 구현은 했는데 중간에 테스트 케이스 틀리는게 있어서 블로그 도움 받아서 참고용으로 올렸습니다!

def numToXy(num):	#숫자->좌표 변환 함수
    p_cnt = 0 # 그룹 확인 변수
    xyArr = [0, 0] # x, y 저장
    total_p = 0 # 1~ p_cnt 까지 총합을 저장한 변수, 그룹의 마지막수		
    num2 = num
    while True: # p_cnt 값을 늘려나가며 num2에서 p_cnt를 뺀다. 
        p_cnt += 1
        total_p += p_cnt
        num2 -= p_cnt	
        if num2 <= 0: # num2의 값이 0 이나 음수이면 해당 p_cnt가 num의 그룹이 된다.
            xyArr[0] = p_cnt-(total_p-num) # x 좌표, x 좌표값은 1~ i까지 증가, i에서 그룹 내 가장 큰수 - 구하고자 하는 숫자
            xyArr[1] = 1+(total_p-num) # y 좌표, y 좌표값음 i에서 1씩 감소, 1에 그룹 내 가장 큰수와 구하고자 하는 수의 차이를 더해서 구함
            break
    return xyArr
def xyToNum(x, y):	#좌표->숫자 변환 함수
    group = (x+y)-1 #  각 그룹 =  두 좌표의 합 -1
    total = 0 # 최댓값
    for i in range(1, group+1):
        total += i 
#         좌표가 속한 값을 구하고 y의 좌표 값이 1부터 커지는 원리를 이용해 그룹의 최댓값을 구한다.
# y좌표는 그룹의 최댓값에서부터 1씩 감소하는 특징이 있기 때문에 최댓값과 현재 좌표를 이용하면 num을 구할 수 있다.
#         total += i
    return total - (y-1) # 최댓값 - (y-1) = 현재 좌표가 가리키는 num
T = int(input())
for test_case in range(1, T+1):
    p, q = map(int, input().split())
    a = numToXy(p)
    b = numToXy(q)
    x = a[0] + b[0]
    y = a[1] + b[1]
    print("#{} {}".format(test_case, xyToNum(x, y)))