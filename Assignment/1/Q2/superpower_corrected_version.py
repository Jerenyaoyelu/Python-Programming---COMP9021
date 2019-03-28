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

def find_elemt(l, e):
    for i in range (len(l)):
        if l[i]==e:
            return i

def Q1(l,nb):
    t_l = l
    while nb>0:
        t_l[find_elemt(t_l,min(t_l))] = t_l[find_elemt(t_l,min(t_l))]*(-1)
        nb -=1
    return sum(t_l)
    
def Q2(l,nb):
    greatest_sum=0
    while nb > 0:
        greatest_sum += min(l)*(-1)
        l.remove(min(l))
        nb -=1
    return greatest_sum+sum(l)
greatest_achievable_power[0]=Q1(heros_power_l,nb_of_switches)
heros_power_l= list(map(int,heros_power.split()))
greatest_achievable_power[1]=Q2(heros_power_l,nb_of_switches)
heros_power_l= list(map(int,heros_power.split()))

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
        
p_l = {(get_position_of_least_chunk(heros_power_l,i),i) for i in range(1, len(heros_power_l)+1)}
sum_l =[sum(heros_power_l)]
for e in p_l:
    s = 0
    for i in range(len(heros_power_l)):
        if i>=e[0] and i<=(e[0]+e[1]-1):
            s+=heros_power_l[i]*(-1)
        else:
            s +=heros_power_l[i]
    sum_l.append(s)
    if e[1] == nb_of_switches:
        greatest_achievable_power[2] = s
greatest_achievable_power[3] = max(sum_l)
print(f'Possibly flipping the power of the same hero many times, \
the greatest achievable power is {greatest_achievable_power[0]}.')
print(f'Flipping the power of the same hero at most once, \
the greatest achievable power is {greatest_achievable_power[1]}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, \
the greatest achievable power is {greatest_achievable_power[2]}.')        
print(f'Flipping the power of arbitrarily many consecutive heroes, \
the greatest achievable power is {greatest_achievable_power[3]}.')     

