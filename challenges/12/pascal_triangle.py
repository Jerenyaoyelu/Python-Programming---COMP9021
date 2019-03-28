# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.

import sys

# Insert you code here            
def produce_triangle(N):
    l=[[]]*(N+1)
    if N==0:
        return [[1]]
    elif N==1:
        return [[1],[1,0,1]]
    else:
        l[0]=[1]
        l[1]=[1,1]
        for i in range(2,N+1):
            sub_l=[0]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    sub_l[j]=1
                else:
                    sub_l[j]=l[i-1][j-1]+l[i-1][j]
            l[i]=sub_l
    return l
try:
    N=int(input('Enter a number: '))
    if N < 0:
        raise TypeError
except TypeError:
    print('Incorrect input, giving up.')
    sys.exit()
elmt_l=produce_triangle(N)
unit_width=len(str(max(elmt_l[-1])))
row_width=unit_width*(len(elmt_l[-1])*2-1)
for i in range(N+1):
    s=''
    for j in range(len(elmt_l[i])):
        if j==len(elmt_l[i])-1:
            s +=' '*(unit_width-len(str(elmt_l[i][j])))+str(elmt_l[i][j])
        else:
            s +=' '*(unit_width-len(str(elmt_l[i][j])))+str(elmt_l[i][j])+' '*unit_width
    space_str=' '*(((row_width-len(s)))//2)
    string=space_str+s
    print(string)
   
