# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here
from math import sqrt


def compute_prime(n):
    prime_l=[True]*n
    prime_l[0]=False
    prime_l[1]=False
    for i in range(2,round(sqrt(n))+1):
        if prime_l[i]==True:
            for j in range(i+1,n):
                if j%i==0 and prime_l[j]==True:
                    prime_l[j]=False
    return prime_l

def get_five_dig_prime_list(l):
    five_dig_l=[]
    for i in range(10000,len(l)):
        if l[i]==True:
            five_dig_l.append(i)
    return five_dig_l

five_dg_prime_l=get_five_dig_prime_list(compute_prime(100_000))
print('The solutions are:\n')
for i in range(len(five_dg_prime_l)-5):
    t=(five_dg_prime_l[i]-five_dg_prime_l[i],five_dg_prime_l[i+1]-five_dg_prime_l[i],\
       five_dg_prime_l[i+2]-five_dg_prime_l[i],five_dg_prime_l[i+3]-five_dg_prime_l[i],\
       five_dg_prime_l[i+4]-five_dg_prime_l[i],five_dg_prime_l[i+5]-five_dg_prime_l[i])
    if t==(0,2,6,12,20,30):
        print(f'{five_dg_prime_l[i]} {five_dg_prime_l[i+1]} {five_dg_prime_l[i+2]} {five_dg_prime_l[i+3]} {five_dg_prime_l[i+4]} {five_dg_prime_l[i+5]}\n')

