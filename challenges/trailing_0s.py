# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial, sqrt

nb=int(input('Input a nonnegative integer: '))
if nb < 0:
    print('Incorrect input, giving up.')
    sys.exit()
def DivisionM (nb):
    count=0
    temp=factorial(nb)
    while temp%10==0:
        count +=1
        temp = temp //10
    return count
print(f'Computing the number of trailing 0s in {nb}! by dividing by 10 for long enough: {DivisionM(nb)}')

def StringM (nb):
    temp=str(factorial(nb))
    for i in range(len(temp)-1,-1,-1):
        if int(temp[i])!=0:
            return len(temp)-1-i
print(f'Computing the number of trailing 0s in {nb}! by converting it into a string: {StringM (nb)}')

def find_prime (n):
    l=[True]*(n+1)
    l[0]=False
    l[1]=False
    for i in range(2,round(sqrt(n))+1):
        if l[i]:
            for j in range (i+1,n+1):
                if j%i==0:
                    l[j]=False
    prime_l=[i for i in range(len(l)) if l[i] == True]
    return prime_l
def prime_decomp (n):
    prime_l=find_prime(n)
    prime_d=[]
    for e in prime_l:
        while n%e==0:
            n=n//e
            prime_d.append(e)
    return prime_d
def Smartway (nb):
    count=0
    for i in range(1,nb+1):
        temp=prime_decomp(i)
        count +=temp.count(5)
    return count
print(f'Computing the number of trailing 0s in {nb}! the smart way: {Smartway (nb)}')
        
        
        
        
    
    