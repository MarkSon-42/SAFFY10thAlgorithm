# 5431. 민석이의 과제 체크하기

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    
    did = list(map(int, input().split())) # 한 사람 번호
    did.sort() # 한 사람들 번호 정렬

    people = [i for i in range(1, N+1)] # n명의 번호 리스트 생성
    did_not = []
    for j in people: # 안한 사람들 번호를 안한 사람들 리스트에 넣기
        if j not in did:
            did_not.append(j)
    did_not.sort()
    did_not = list(map(str, did_not))
    did_not = ' '.join(did_not)
    
    print("#{} {}".format(test_case, did_not))