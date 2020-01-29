lst = list(map(int,input().split()))
N = len(lst)
half = N//2
if(N==3 and half == 1): #for cases where length of the list is 3 and we have a value repeating twice
    half =2

for i in range(N):
    count = 0
    x = lst[i]
    for j in range(i,N):
        if(lst[j] == x):
            count +=1
     
    if(count>=half):
        print(lst[i])
    


