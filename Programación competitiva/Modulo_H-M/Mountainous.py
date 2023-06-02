N = int(input());
mountainous = [int(input()) for _ in range(N)];
Longest = 0;

for i in range(1, N-1):
    count = 0;
    j = i;
    k = 0;
    
    while(j < N and (j-k) >= 0 and mountainous[i] > mountainous[i+1]):  
        
        if(mountainous[j] == mountainous[j - k] and (mountainous[j] < mountainous[j-1]) or mountainous[i] == mountainous[j]):
            count+=1;
        else:
            break;
        k+=2;
        j+=1;
    
    if(count > Longest and count != 1):
        Longest = count;

Longest = Longest*2 - 1;
print(Longest);