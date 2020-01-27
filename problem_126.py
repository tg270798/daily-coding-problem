def ins_op(lst,N,k):
    i=0
    temp = k
    while(k!=0):
        
        x = lst[i]
        lst.insert(N+i+1,x)
        i = i+1
        k = k-1
    
    del lst[0:temp]
        
    return lst

lst = list(map(int,input().split()))
N = len(lst)
k = int(input())
print(ins_op(lst,N,k))
