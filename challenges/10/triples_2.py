# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here
from math import sqrt

l=[False]*900
for i in range(round(sqrt(1000))+1):
    for j in range(round(sqrt(1000))+1):
        if (i**2+j**2)>=100 and (i**2+j**2)<=999:
            l[(i**2+j**2)]=1
for i in range(len(l)-2):
    if (l[i]+l[i+1]+l[i+2])==3:
        print(i,i+1,i+2)
