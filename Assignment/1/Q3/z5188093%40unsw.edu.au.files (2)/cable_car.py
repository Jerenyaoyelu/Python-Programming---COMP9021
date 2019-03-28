import os.path
import sys

from collections import defaultdict

file_name=input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(file_name):
    print('Sorry, there is no such file.')
    sys.exit()
with open (file_name) as file:
    file_content=file.read()
try:
    file_l=list(map(int,file_content.split()))
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
if len(file_l)<2:
    print ('Sorry, input file does not store valid data.')
    sys.exit()
def isincreasing(l):
    temp=0
    for e in l:
        if e>0:
            if e<=temp:
                print ('Sorry, input file does not store valid data.')
                sys.exit()
            else:
                temp=e
        else:
            print ('Sorry, input file does not store valid data.')
            sys.exit()
isincreasing(file_l)

ride=[]
longest_ride=0
removed_pillars=0
greatest_nb_of_pillars=0

def compute_ride(l):
    t_ride=[]
    i=0
    while i<=len(l)-1:
        ride_len=1
        first_p=i
        slope_gap=l[i+1]-l[i]
        if len(l)==2:
            t_ride.append([first_p,slope_gap,ride_len])
            break
        for j in range(i+1,len(l)-1):
            if l[j+1]-l[j]==slope_gap:
                ride_len +=1
            else:
                i=j
                t_ride.append([first_p,slope_gap,ride_len])
                break
        if j==len(l)-2:
            t_ride.append([first_p,slope_gap,ride_len])
            break
    return t_ride
#list of list storing fisrt pillar's position, the slope and the max length of ride.
ride=compute_ride(file_l)
#get the longest ride
for e in ride:
    if e[2]>longest_ride:
        longest_ride=e[2]
#list of dictionary storing every "slope:nb_of_related_pillars"
slope_list=[]
#this function is to find the corresponding slope in the pillar which is being 
#computed for the slope with the most current pillar
def find_slope(dic,slope):
    if slope in dic.keys():
        return dic[slope]
    else:
        return 0
#this function is to compute the slope between every previous pillar and the
#current one, and return a dictionary storing every slope and the number of 
#related pillars(starts from the very first one).
def compute_slope(slope_l,l,index):
    slope_dic={}
    for i in range(index-1,-1,-1):
        if find_slope(slope_l[i],l[index]-l[i])==0:
            slope_dic[l[index]-l[i]]=2
        else:
            slope_dic[l[index]-l[i]] = find_slope(slope_l[i],l[index]-l[i])+1
    return slope_dic
if len(ride)==1:
    print('The ride is perfect!')
    longest_ride=ride[0][2]
else:
    print('The ride could be better...')
    #get the list of of dictionary storing every "slope:nb_of_related_pillars"
    for i in range(len(file_l)):
        slope_list.append(compute_slope(slope_list,file_l,i))
    #get the minimal number of pillars to remove
    for e in slope_list:
        if len(e.values())>0:
            if max(e.values())>=greatest_nb_of_pillars:
                greatest_nb_of_pillars=max(e.values())
    removed_pillars=len(file_l)-greatest_nb_of_pillars
print(f'The longest good ride has a length of: {longest_ride}')
print(f'The minimal number of pillars to remove to build a perfect ride \
from the rest is: {removed_pillars}')
