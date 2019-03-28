from math import sqrt
def get_prime_generator(nb):
    l=[True]*(nb+1)
    for i in range(2,round(sqrt(nb))+1):
        if l[i]:
            e=i+i
            while e<=nb:
                l[e]=False
                e +=i
    return list((i for i in range(2,nb+1) if l[i]))
