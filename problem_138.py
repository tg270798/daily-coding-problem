def ret_coin(N):
    count = 0
    
    while(N!=0):
        if(N>=25):
            N= N-25
            count = count +1 
        elif((N>=10) and (N<25)):
            N = N - 10
            count =count +1
        elif((N>=5) and (N<10)):
            N = N - 5
            count = count + 1
        elif((N>=1) and (N<5)):
            N = N -1
            count = count +1
    
    return count

cent = int(input())
print(ret_coin(cent))
