#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:59:59 2018

@author: luyaoye
"""
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
##？？what if hight is not successive num? so this is wrong way to add hight in to dict.
##no, in fact, doesnt matter. I just use this to compute capcity of water every level,
##although useing other way(not storing missing heights) may be nicer.
for i in range(min(file_cts),max(file_cts)+1):
    land_H_d.setdefault(i,file_cts.count(i))
'''
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
'''
#计算每一层的水容量，需输入前面存储高度和次数的字典，以及高度    
def cap_of_each_level(dic,h_level):
    #每一层水的总容量
    cap=0
    for e in dic.keys():
        if e <=h_level:
            cap +=dic[e]
    return cap

#方法1：（逻辑还是有问题，如何Height并不是连续的呢？这段代码执行就有问题了。）
#问题已解决，因为优化了得到前面存储高度和次数的字典的逻辑
#到当前高度层的总储水量
for e in land_H_d.keys():
    if water > cap_of_each_level(land_H_d,e):
        water -= cap_of_each_level(land_H_d,e)
        #注意：即使剩余水量小于下一层储水量时（甚至已为0），e仍然会加到下一层，
        #只要在总高度之内
    else:
        #in the current level, the height that water can reach(not including
        #the height of level).
        H_now=round((water/cap_of_each_level(land_H_d,e)),2)
        #此处高度应该为上一层高度(所以要减1单位高度)
        #it's logic error。
        #I did not use index in the loop， so i cannot simplily use 'e-1' to get the hight of last level！！！
        #this  is rubbish！！！
        reached_Height=e-1+H_now+min(land_H_d.keys())
        print(e-1)
        break
    #case that total amount of water exceeds the total capacity of this land.
    if e==max(land_H_d.keys()):
        reached_Height=round(water/sum(land_H_d.values()),2)+e+min(land_H_d.keys())
        print(min(land_H_d.keys()))
print(f'The water rises to {reached_Height:.2f} centimetres.')
        
