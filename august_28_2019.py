def prodreturn(lis):
    lisreturn = []
    #prod = 1
    for i in range(len(lis)):
        prod =1
        for j in range(len(lis)):
            prod = prod * lis[j]
        result = prod // lis[i]
        lisreturn.insert(i,result)
    
    
    return lisreturn 


N = int(input())
lis = []
for i in range(N):
    x = int(input())
    lis.insert(i,x)

print(prodreturn(lis))
