import sys
import os
from collections import Counter

file_name= input('Which data file do you want to use?')
if not os.path.exists(file_name):
    print("Sorry, no such file.")
    sys.exit()
water = int(input('How many decilitres of water do you want to pour down?'))
if water < 0:
    print("Sorry, illegal input!")
    sys.exit()
    
reached_Height=0
#this function is able to transfer a string containing numbers and separators to 
#a list of integers without separators.
def rmsep_to_intlist(string):
    rm_separator=string.split()
    to_list=list(map(int,rm_separator))
    return to_list
with open(file_name) as file:
    file_conts_rs=file.read()   
#list of all heights
land_H_d=dict(Counter(rmsep_to_intlist(file_conts_rs)))
#计算每一层的水容量，需输入前面存储高度和次数的字典，以及高度    
def cap_of_each_level(dic,h_level):
    #每一层水的总容量
    cap=0
    for e in dic:
        if e < h_level:
            cap += dic[e]*(h_level-e)
    return cap

def area_of_current_level(dic, h_level):
    area=0
    for e in dic:
        if e < h_level:
            area += dic[e]
    return area

i=min(land_H_d)
while i >=0:
    i +=1
    if water <= area_of_current_level(land_H_d,i):
        reached_Height = round(water/area_of_current_level(land_H_d,i),2) + i-1
        break
    else:
        water -= area_of_current_level(land_H_d,i)
    if i == max(land_H_d):
        reached_Height = round(water/area_of_current_level(land_H_d,i+1),2) + i
        break
print(f'The water rises to {reached_Height:.2f} centimetres.')
