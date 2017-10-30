n=int(input())
z=0
for i in range(4, n+1):
    for j in range(4, i+1):
        nsum = 0
        x=pow(i,j)
        while x>0:
            y=x%10
            nsum=nsum+y
            x=x/10;
        if nsum > z:
            z = nsum
print (z)
