Request = int(input("Ingrese N request:  "));
PascalRange = 3;
Pascal = [
    [1 , 0],
    [1 , 1, 0]
]

for i in range(Request):
    
    PascalBoolean = -1;
    Num = int(input("Ingrese N buscar:  "));
    
    while (PascalBoolean == -1):
        
        Pascal.append([1]*PascalRange);
        
        for j in range(1, PascalRange):
            
            Pascal[PascalRange-1][j] = Pascal[PascalRange-2][j] + Pascal[PascalRange-2][j-1];
        
        Pascal[PascalRange-1].append(0);
        Co = 2;
        
        for j in range(PascalRange):
            
            for k in range(Co):
                
                if(Num == Pascal[j][k] and PascalBoolean == -1):
                    
                    PascalBoolean = j;
                    print(j+1);
                
            Co+=1;
        
        PascalRange+=1;