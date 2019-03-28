

import sys
from random import seed, randrange


try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
fgl = 0
sfl = 0
lgf = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
#first_and_last is the set of recording the most times of repeated tuple
#of first and last digit of the member of L?
first_and_last = set()

# REPLACE THIS COMMENT WITH YOUR CODE

print()
print('x is:', x)
print('L is:', L)
print()
list_x=list(str(x))
for i in range(len(list_x)):
	sum_of_digits_in_x +=int(list_x[i])
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
for i in range(len(L)):
    nb=len(list(str(L[i])))
    if L[i]//(10**(nb-1))>L[i]%10:
        fgl +=1
    elif L[i]//(10**(nb-1))==L[i]%10:
        sfl +=1
    else:
        lgf +=1
print(f'There are {fgl}, {sfl} '
      f'and {lgf} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
#mmb_set_l is the list storing the set of every member of L
mmb_set_l=[set(str(L[i])) for i in range(len(L))]

#dgcount is the list storing the number of distinct digits of member of L
dgcount=[len(list(mmb_set_l[i])) for i in range(len(L))]

#This is assgining the repeating times of each member in the list\
#of dgcount to the corresponding value of member of distinct_digits.
for i in range(len(dgcount)):
    distinct_digits[dgcount[i]]=dgcount.count(dgcount[i])
for i in range(1, 9):
    if distinct_digits[i]>0:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
for i in range(len(L)):
    nb=len(list(str(L[i])))
    if max_gap<abs(L[i]//(10**(nb-1))-L[i]%10):
        max_gap=abs(L[i]//(10**(nb-1))-L[i]%10)
    if min_gap>abs(L[i]//(10**(nb-1))-L[i]%10):
        min_gap=abs(L[i]//(10**(nb-1))-L[i]%10)       
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
mmb_tuple=(0,0)
fl_list=[]
for e in L:
    #this is recording the list of digits from the each member of L
    mmb_l_list=list(str(e))
    mmb_tuple=(int(mmb_l_list[0]),int(mmb_l_list[len(mmb_l_list)-1]))
    #This is the list recording the tuple of first and last digit
    fl_list.append(mmb_tuple)
#pcd is a dictionary recording the pairs of (f,l) as the key\
#and its repeating times as the value.
pcd=dict([(e,fl_list.count(e)) for e in fl_list])
'''
for e in fl_list:
    if pcd[e]==max(pcd.values()):
        first_and_last.add(e)
'''
# Why does this command output a generetor not a tuple? But 'e' in the fl_list is a tuple.
first_and_last = [e for e in fl_list if pcd[e]==max(pcd.values())]
##'first_and_last.add(e for e in fl_list if pcd[e]==max(pcd.values()))'
##'e for e in fl_list if pcd[e]==max(pcd.values())' is a list, so this command is kind of\
##adding the whole list

'''
def get_key(d,v):
    for e in fl_list:
        if pcd[e]==v:
            print (e)
first_and_last.add(get_key(pcd,max(pcd.values())))
'''
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
