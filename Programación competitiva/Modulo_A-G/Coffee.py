N = int(input());
I = input();
I = list(I);
C = 0;
for i in range(N):
    
    if(I[i] == "1"):
        
        C+=1;
        D = 0;
        
        for j in range(i+1, N):
            
            if(I[j] == "1" or D == 2):
                break;
            else:
                C+=1;
            
            D+=1;

print(C);