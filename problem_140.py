def copy_finder(lst):
    ret_lst = []
    N = len(lst)
    for i in range(N):
        count = 0
        ele = lst[i]
        for j in range(N):
            if(ele == lst[j]):
                count =count +1
        if(count == 1):
            ret_lst.append(lst[i])
        
    return ret_lst         
       
    

lst = list(map(int,input().split()))
print(copy_finder(lst))
