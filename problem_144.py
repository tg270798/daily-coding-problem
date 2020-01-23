def sorting(lis):
    for i in range(len(lis)):
        min_ele = lis[i]
        for j in range(i+1,len(lis)):
            if(lis[j] < min_ele):
                min_ele = lis[j]
                lis[i],lis[j] = lis[j],lis[i]
       
    return lis     
        
    
def second_greatest(lis,index):
    sort_list = list(sorting(lis))
    if(index >= len(lis)-1):
        return None
    else:
        return lis[index+1]
    #sort_list = sorting(lis)
    #print(sort_list)
    
    
lis = list(map(int,input().split()))
index = int(input())
print(second_greatest(lis,index))
