def arrange(lst,pivot):
    N = len(lst)
    sec_lst = []
    j = 0
    mid = N//2
    
    #first arrange the pivot element to the middle of the second list.
    for i in range(N):
        if(lst[i] == pivot):
            sec_lst.insert(mid,lst[i])
            mid = mid +1
    #now compare and arrange the elements of the list accordingly
    for i in range(N):
        if(lst[i] < pivot):
            sec_lst.insert(j,lst[i])
            j = j+1
        elif(lst[i] > pivot):
            sec_lst.insert(mid,lst[i])
            mid = mid + 1
    return sec_lst

lst = list(map(int,input().split()))
pivot = int(input())
print(arrange(lst,pivot))
