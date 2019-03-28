# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.
import sys

# Insert your code here
try:
    n=int(input('Input a strictly positive number:'))
except TypeError:
    print('Incorrect input,giving up.')
    sys.exit()
if n <=0:
    print('Incorrect input,giving up.')
    sys.exit()
def produce_str(n,mode=1):
    s=''
    if mode==1:
        for i in range(n-1):
            s +=chr(int((((n-1)*n)/2)+i)%26+65)
    if mode==-1:
        for i in range(n):
            s = chr(int((((n-1)*n)/2)+i)%26+65)+s
    return s
for i in range(1,n+1):
    zero_str=' '*(n-i)
    left_str=produce_str(i,1)
    right_str=produce_str(i,-1)
    string=zero_str+left_str+right_str
    print(string)
