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
#this is to remove the minimum and return the minimum and its counted number.
def count_min(l_nb):
    count=0
    for e in l_nb:
        if e==min(l_nb):
            count +=1
    return (min(l_nb),count)    
#删除所有指定元素，并返回新列表
def del_all_e (l_nb,e):
    while True:
        if e not in l_nb:
            break
        else:
            l_nb.remove(e)
    return l_nb
#list of all heights
file_cts=rmsep_to_intlist(file_conts_rs)
land_H_d={}
#这个循环可以得到从低到高的所有高度和对应的数量，并存储在一个字典里
#这个循环语句需要优化，时间效率不行
while file_cts!=[]:
    #tuple of minimal height and its counted number
    H_C=count_min(file_cts)
    #dictionry of all heights and its counted number
    #setdefault() is an amazing method, memorize it!!
    land_H_d.setdefault(H_C[0],H_C[1])
    #delete minimal heights
    file_cts=del_all_e(file_cts,H_C[0])
#计算每一层的水容量，需输入前面存储高度和次数的字典，以及高度    
def cap_of_each_level(dic,h_level):
    #每一层水的总容量
    cap=0
    for e in dic.keys():
        if e <=h_level:
            cap +=dic[e]
    return cap
'''
#方法1：（逻辑还是有问题，如何Height并不是连续的呢？这段代码执行就有问题了。）
#问题出在前面的while循环得出的字典里
#因为按照这个逻辑得出的字典所存储的高度并不一定是连续的，次数为0的高度也就直接被忽略了
#所以程序运行的最终结果会出现问题！！
#到当前高度层的总储水量
##this is an example of rubbish code。 details see rubbish_rain.py
for e in land_H_d.keys():
    if water > cap_of_each_level(land_H_d,e):
        water -= cap_of_each_level(land_H_d,e)
        #注意：即使剩余水量小于下一层储水量时（甚至已为0），e仍然会加到下一层，
        #只要在总高度之内
    else:
        #in the current level, the height that water can reach(not including
        #the height of level).
        H_now=round((water/cap_of_each_level(land_H_d,e)),2)
        #此处高度应该为上一层高度
        reached_Height=e-1+H_now+1
        break
    #case that total amount of water exceeds the total capacity of this land.
    if e==max(land_H_d.keys()):
        reached_Height=round(water/sum(land_H_d.values()),2)+e+min(land_H_d.keys())    
'''
#方法2:（运行成功）
##this one may be even worse，it ends up with dead loop for last 4 testcases， for some  results appears better though。
h_l=list(land_H_d.keys())
sum_cap=0
for i in range(len(h_l)):
    if sum_cap<water:
        sum_cap += cap_of_each_level(land_H_d,h_l[i])
    else:
        sum_cap -= cap_of_each_level(land_H_d,h_l[i-1])
        water -=sum_cap
        H_now=water/cap_of_each_level(land_H_d,h_l[i-1])
        reached_Height=h_l[i-1]+H_now
        break
    if i==len(h_l)-1:
        reached_Height=(water-sum_cap)/sum(land_H_d.values())+h_l[i]
'''        
##备注：
h_l=land_H_d.keys()
sum_cap=0
for i in range(len(h_l)):
    sum_cap += cap_of_each_level(land_H_d,h_l[i])
    if sum_cap > water:
        p_cap=sum_cap - cap_of_each_level(land_H_d,h_l[i])
        H_now=(water-p_cap)/cap_of_each_level(land_H_d,h_l[i-1])
        reached_Height=h_l[i-1]+H_now
        break  
这段代码会发生一下错误：
    TypeError: 'dict_keys' object does not support indexing
这是由于python3改变了dict.keys,返回的是dict_keys对象,支持iterable 
但不支持indexable，我们可以将其明确的转化成list。
##
'''


'''
#方法3:（还未运行成功）
#判断水是否够注满当前高度，并返回可到达高度
def water_pouring (water, ):
    if water < units:
        H=round(water/units,2)
        water -=units
    else:
        water -=units
        H = 1
    print(water)
    print(H)
    return water,H
for e in h_l:
    if water < land_H_d[e]:
        
    water, H_temp=water_pouring(water,land_H_d[e])
    reached_Height +=H_temp
    if water < 0:
        break
reached_Height += min(h_l)
'''
print(f'The water rises to {reached_Height:.2f} centimetres.')



    

