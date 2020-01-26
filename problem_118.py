def sort(lst,N):
    for i in range(N):
        min_ele = lst[i]
        for j in range(i+1,N):
            if(lst[j]<min_ele):
                min_ele = lst[j]
                lst[i],lst[j] = lst[j],lst[i]    
    return lst
                #pass

def square(lst,N):
    lis = []
    #sort_lst = []
    for i in range(N):
        sq_lst = lst[i] **2
        lis.insert(i,sq_lst)
    #sort_lst = sort(lis,N)
    #return sort_lst
    return sort(lis,N)
    #pass

lst= list(map(int,input().split()))
N= len(lst)

print(square(lst,N))
