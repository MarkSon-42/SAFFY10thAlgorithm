# 1244. 최대 상금
# dfs, 백트래킹, 딕셔너리 사용하였고 처음에는 시간 초과로 인해 실패하다가 중복 되는 과정을 없애기 위해서 가지치기 방법을 구글링을 통해 참고하여 해결 하였습니다.
# 경우의 수를 만들어 dfs 방식으로 탐색하며 최댓값을 계속 갱신해서 최대 교환 횟수에 오면 금액 최댓값을 반환하는 방식

def dfs(change):
    global max_money 
    if change == max_change: # 교환 횟수가 최대 교환 횟수와 같아지면
        changed = ''.join(num_table) # 바꾼 숫자판을 문자열로 변환
        max_money = max(max_money, changed) # 금액 최댓값은 금액 최댓값과 바꾼 숫자판을 문자열로 변환한 것중 큰 것을 최댓값으로 갱신
        return 
    
    for i in range(len(num_table)): # 두 개씩 뽑아서 조합을 만들어 비교한다. 
        for j in range(i+1, len(num_table)):
            num_table[i], num_table[j] = num_table[j], num_table[i] # 교환
            changed = ''.join(num_table) # 숫자판을 바꾸면 합쳐서 문자열로 만들어서 비교
            if visited.get((changed, change), 1): # 가지치기 : visited에 (바꾼 숫자판, 교환 횟수) key가 없으면 1로 처리 -> 방문한 적이 없으면 1 
                visited[(changed, change)] = 0 # 방문을 하면 0으로 바꿔 다음에 다시 방문하지 않게 처리 (방문했던 곳 중복 방지)
                dfs(change+1) # 바꾼 횟수 +1해서 dfs 다시 호출
            num_table[i], num_table[j] = num_table[j], num_table[i] # 다른 경로 탐색을 위해 다시 i, j 돌려놓기

T = int(input())
for test_case in range(1, T + 1):
    num_table, max_change = input().split() # 숫자판, 교환 횟수
    num_table = list(num_table)
    max_change = int(max_change)
    max_money = "0" # 금액의 최댓값
    visited = {} # 방문했는지 확인하는 딕셔너리
    dfs(0)
    print("#{} {}".format(test_case, max_money))