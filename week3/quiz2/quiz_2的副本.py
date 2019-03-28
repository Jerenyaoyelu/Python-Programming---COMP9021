# Written by *** and Eric Martin for COMP9021



import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE
def get_simplest_fraction(a,b):
    if a<=b:
        return(int(a/gcd(a,b)),int(b/gcd(a,b)))
    else:
        return(int(b/gcd(a,b)),int(a/gcd(a,b)))
def get_value(a,b):
    if a<=b:
        return float(a/b)
    else:
        return float(b/a)
def get_size_from_nb(nb):
    return len(str(nb))
f_pairs_l=set([get_simplest_fraction(L[i],L[j]) for i in range(len(L)) for j in range(len(L))])
# this dictionary records every smpliest fraction pairs and its size.
size_f_dict=dict([(e,get_size_from_nb(e[0])+get_size_from_nb(e[1])) for e in f_pairs_l])
# this list records every tuple of numerator and denominator.
size_l=[(get_size_from_nb(e[0])+get_size_from_nb(e[1])) for e in f_pairs_l]
size_of_simplest_fraction=min(size_l)
size_of_most_complex_fraction=max(size_l)
print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
simplest_before_sort=[]
complex_before_sort=[]
for e in f_pairs_l:
    if size_f_dict[e]==min(size_l):
        simplest_before_sort.append(e)
    if size_f_dict[e]==max(size_l):
        complex_before_sort.append(e)
#lambda is a amazing function, be master of it.
simplest_fractions=sorted(simplest_before_sort, key=lambda x:x[0]/x[1])
most_complex_fractions=sorted(complex_before_sort,key=lambda x:x[0]/x[1],reverse=True)
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))

latter_denominators_l=set(y for (x,y) in most_complex_fractions)
#this dictionary records the every prime factor and its multiplicity。
pf_and_m_of_deno={}
from math import sqrt
'''
def get_prime(nb):
    l=[True]*(nb+1)
    for i in range(2,round(sqrt(nb))+1):
        if l[i]:
            e=i+i
            while e<=nb:
                l[e]=False
                e +=i
    return list((i for i in range(2,nb+1) if l[i]))
''''
#this loop aims to transfer the denominators in the list of 'latter_denominators_l'
#into the form of the multiple of several prime factors.
'''
for e in latter_denominators_l:
    p_l=get_prime(e)
    count_p=0
    for i in range(len(p_l)):
        #this loop is to find every prime factor and to record them in the dictionary
        while e%p_l[i]==0:
            e=e/p_l[i]
            count_p +=1
            # this conditional statement is to see that if the prime 'p' is a member
            # of the dictionary 'pf_and_m_of_deno'。
            if p_l[i] in pf_and_m_of_deno.keys():
                if pf_and_m_of_deno[p_l[i]]<count_p:
                    pf_and_m_of_deno[p_l[i]]=count_p
            else:
                pf_and_m_of_deno[p_l[i]]=count_p
        count_p=0
'''
def get_prime_generator(nb):
    l=[True]*(nb+1)
    for i in range(2,round(sqrt(nb))+1):
        if l[i]:
            e=i+i
            while e<=nb:
                l[e]=False
                e +=i
    return (i for i in range(2,nb+1) if l[i])

for e in latter_denominators_l:
    p=next(get_prime_generator(e))
    count_p=0
    while e>1:
        #this loop is to find every prime factor and to record them in the dictionary
        while e%p==0:
            e=e/p
            count_p +=1
            # this conditional statement is to see that if the prime 'p' is a member
            # of the dictionary 'pf_and_m_of_deno'。
            if p in pf_and_m_of_deno.keys():
                if pf_and_m_of_deno[p]<count_p:
                    pf_and_m_of_deno[p]=count_p
            else:
                pf_and_m_of_deno[p]=count_p
        count_p=0
        p=next(get_prime_generator(int(e)))
        print(p)

lpf_before_sort=[]
if pf_and_m_of_deno=={}:
    largest_prime_factors=[]
    multiplicity_of_largest_prime_factor=0
else:
    multiplicity_of_largest_prime_factor=max(pf_and_m_of_deno.values())
    for e in pf_and_m_of_deno.keys():
        if pf_and_m_of_deno[e]==max(pf_and_m_of_deno.values()):
            lpf_before_sort.append(e)
largest_prime_factors=sorted(lpf_before_sort)
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
        
        
