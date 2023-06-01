N = input();
N = N.split(" ");
N = [int(i) for i in N];
R = input();
R = list(R);
i = N[1];
j = 0;
k = "L";
while(i > 0 and j < N[0]):
    if(k == R[j]):
        j+=1;
    else :
        i-=1;
    if(k == "L"):
        k = "R"
    else :
        k= "L"
print(i);