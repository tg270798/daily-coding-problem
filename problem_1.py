def numChecker(lis,K):
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[j]+lis[i] == K):
                print("True")
                break
            

lis = list(map(int,input().split()))
K = int(input())
numChecker(lis,K)
