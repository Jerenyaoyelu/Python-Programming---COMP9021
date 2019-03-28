import os.path
import sys
from time import time
from collections import deque

file_name=input('Please enter the name of the file you want to get data from: ')
start=time()
if not os.path.exists(file_name):
    print('Sorry, no such file.')
    sys.exit()
with open(file_name) as file:
    file_context=file.readlines()
file_data=[]
for e in file_context:
    temp=e.strip()
    try:
        if list(map(int,temp.split()))!=[]:
            file_data.append(list(map(int,temp.split())))
    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()
if len(file_data)!=2:
    print('Sorry, input file does not store valid data.')
    sys.exit()
def isvalid_data(l):
    line_len=len(l[0])
    if line_len<2:
        print('Sorry, input file does not store valid data.')
        sys.exit()
    for line in l:
        if len(line)!=line_len:
            print('Sorry, input file does not store valid data.')
            sys.exit()
    for e in list(zip(*l)):
        if e[0]<=e[1]:
            print('Sorry, input file does not store valid data.')
            sys.exit()
isvalid_data(file_data)

distance=0
max_distance=0
def compute_distance(i,l):
    l_ceiling=float('inf')
    h_floor=0
    stop=0
    j=i
    while True:
        if l[0][j]<l_ceiling:
            l_ceiling=l[0][j]
        if l[1][j]>h_floor:
            h_floor=l[1][j]
        if l_ceiling<=h_floor:
            stop=j
            break
        if j>=len(l[0])-1:
            stop=j+1
            break
        j +=1
    return stop-i
distance=compute_distance(0,file_data)
for j in range(len(file_data[0])):
    if max_distance<=compute_distance(j,file_data):
        max_distance=compute_distance(j,file_data)
print(f'From the west, one can see into the tunnel over a distance of {distance}.')
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {max_distance}.')   
end=time()
print(end-start)
    
    
    
    
    
    
