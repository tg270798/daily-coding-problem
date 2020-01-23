def sum1(lis,start,end):
    sublis= []
    add = 0
    sublis = lis[start:end]
    for i in range(len(sublis)):
        add = add + sublis[i]
    
    print(add)



lis =list(map(int,input().split()))
start, end = int(input("starting index ")), int(input("ending index "))
sum1(lis,start,end)
