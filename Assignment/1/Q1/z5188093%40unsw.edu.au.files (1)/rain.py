import sys
import os

file_name= input('Which data file do you want to use?')
if not os.path.exists(file_name):
    print("Sorry, no such file.")
    sys.exit()
water = int(input('How many decilitres of water do you want to pour down?'))
if water < 0:
    print("Sorry, illegal input!")
    sys.exit()
    
reached_Height=0
file_cts=[]
#this function is able to transfer a string containing numbers and separators to 
#a list of integers without separators.
def rmsep_to_intlist(string):
    rm_separator=string.split()
    to_list=list(map(int,rm_separator))
    return to_list
with open(file_name) as file:
    file_conts_rs=file.read()   
#list of all heights
file_cts=rmsep_to_intlist(file_conts_rs)
land_H_d={}
#优化后的代码。。。
for i in range(min(file_cts),max(file_cts)+1):
    land_H_d.setdefault(i,file_cts.count(i))
#计算每一层的水容量，需输入前面存储高度和次数的字典，以及高度    
def cap_of_each_level(dic,h_level):
    #每一层水的总容量
    cap=0
    for e in dic.keys():
        if e <=h_level:
            cap +=dic[e]
    return cap
for e in land_H_d.keys():
    if water > cap_of_each_level(land_H_d,e):
        water -= cap_of_each_level(land_H_d,e)
        #注意：即使剩余水量小于下一层储水量时（甚至已为0），e仍然会加到下一层，
        #只要在总高度之内
    else:
        #in the current level, the height that water can reach(not including
        #the height of level).
        H_now=round((water/cap_of_each_level(land_H_d,e)),2)
        #此处高度应该为上一层高度(所以要减以单位高度)
        reached_Height=(e-1)+H_now+min(land_H_d.keys())
        break
    #case that total amount of water exceeds the total capacity of this land.
    if e==max(land_H_d.keys()):
        reached_Height=round(water/sum(land_H_d.values()),2)+e+min(land_H_d.keys())
print(f'The water rises to {reached_Height:.2f} centimetres.')

    

