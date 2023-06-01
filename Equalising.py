N = int(input());
X = int(input());
a=[0]*N;
y=0;
for i in range(N):
    a[i] = int(input());
    y+= a[i]**2;

y = (N*X/y)**(0.5);

for i in range(N):
    a[i]*=y;
    print(a[i]);