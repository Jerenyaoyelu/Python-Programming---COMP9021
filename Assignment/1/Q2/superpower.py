import sys

heros_power_l=[]
heros_power=input("Please input the heroes'powers: ")
try:
    heros_power_l=list(map(int,heros_power.split()))
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:
    nb_of_switches=int(input('Please input the number of power flips: '))
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
if nb_of_switches<0 or nb_of_switches>len(heros_power_l):
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
greatest_achievable_power=[0]*4
def Q1and2_greatest_power(l,nb,q):
    greatest_sum=0
    new_l=sorted(l)
    for e in new_l:
        if e<0 and nb>0:
            greatest_sum +=e*(-1)
            nb -=1
        elif e>0 and nb>0:
            if q==1:
                greatest_sum +=e*(-1)**(nb)
                nb -=nb
            elif q==2:
                greatest_sum +=e*(-1)
                nb -=1
            else:
                print('Please input correct question number(1 or 2) for the third argument!')
        else:
            greatest_sum +=e
    return greatest_sum
greatest_achievable_power[0]=Q1and2_greatest_power(heros_power_l,nb_of_switches,1)
greatest_achievable_power[1]=Q1and2_greatest_power(heros_power_l,nb_of_switches,2)
def get_position_of_least_chunk(l,nb):
    least_chunk_index=0
    least_sum=float('inf')
    for i in range((len(l)-nb)+1):
        sum_chunk=0
        for j in range(i,i+nb):
            sum_chunk +=l[j]
        if least_sum>=sum_chunk:
            least_sum=sum_chunk
            least_chunk_index=i
    return least_chunk_index
position=0
position=get_position_of_least_chunk(heros_power_l,nb_of_switches)
for i in range(len(heros_power_l)):
    if i>=position and i<=(position+nb_of_switches-1):
        greatest_achievable_power[2] +=heros_power_l[i]*(-1)
    else:
        greatest_achievable_power[2] +=heros_power_l[i]
def get_first_and_last_minus_index(l):
    first_index, last_index,count=0,0,0
    for i in range(len(l)):
        if l[i]<0:
            first_index=i
            break
    for i in range(len(l)):
        if l[i]<0:
            last_index=i
            count +=1
    return first_index, last_index,count
f_minus,l_minus,c_minus=get_first_and_last_minus_index(heros_power_l)
for i in range(len(heros_power_l)):
    if c_minus!=0:
        if i>=f_minus and i<=l_minus:
            greatest_achievable_power[3] +=heros_power_l[i]*(-1)
        else:
            greatest_achievable_power[3] +=heros_power_l[i]
    else:
        greatest_achievable_power[3] +=heros_power_l[i]
print(f'Possibly flipping the power of the same hero many times, \
the greatest achievable power is {greatest_achievable_power[0]}.')
print(f'Flipping the power of the same hero at most once, \
the greatest achievable power is {greatest_achievable_power[1]}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, \
the greatest achievable power is {greatest_achievable_power[2]}.')        
print(f'Flipping the power of arbitrarily many consecutive heroes, \
the greatest achievable power is {greatest_achievable_power[3]}.') 

    

