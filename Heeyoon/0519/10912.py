'''
tc 입력받고
문자열 리스트에 넣고
하나씩 꺼내와서 첫번째원소랑 같은거 찾아서 뽑아서
남은건 배열에 넣고

'''
'''
if wl[j] in wl:
    nmj.append(wl[j])
    wl.remove(wl[j])
wl.remove(wl[j])
'''



tc=int(input())
for i in range(1,tc+1):
    wl=list(input())
    # wl.sort()
    nmj=[]
 
    for j in range(len(wl)):
        if wl[j] not in nmj:
            nmj.append(wl[j])
        else:
            nmj.remove(wl[j])
    nmj.sort() 
 
    if len(nmj)==0: # 다 짝이 있어서 비어있다면   
        print(f'#{i} Good')
    else:    
        a=''
        print(f'#{i} {a.join(nmj)}')
