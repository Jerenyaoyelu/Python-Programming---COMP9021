# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that set of codes the running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by *** and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')
    
def create_code_table(n):
    code_l=[0,-1]
    for i in range(2,n):
        if i%2==0:
            code_l.append(code_l[0]-code_l[i-1])
        else:
            code_l.append(code_l[1]-code_l[i-1])
    return code_l

def decode(encoded_set):
    temp=list(str(bin(encoded_set)))
    binary_l = [temp[i] for i in range(2,len(temp))]
    reversed_binary_l=list(binary_l.__reversed__())
    code_l=create_code_table(len(binary_l))
    s=set()
    for i in range(len(reversed_binary_l)):
        if int(reversed_binary_l[i])==1:
            s.add(code_l[i])
    return sorted(s)

def list_of_nb_to_str(l):
    new_l=list((str(e) for e in l))
    return ''.join(new_l)

def code_derived_set(encoded_set):
    encoded_set=decode(encoded_set)
    new_set=set()
    sum_code=0
    for i in range(len(encoded_set)):
        sum_code +=encoded_set[i]
        new_set.add(sum_code)
    if len(new_set)==0:
        binary_len=1
    else:
        binary_len=max(abs(min(new_set)),abs(max(new_set)))*2+1
    code_table=create_code_table(binary_len)
    derived_temp_binary=[0]*binary_len
    for i in range(binary_len):
        if code_table[i] in new_set:
            derived_temp_binary[i]=1
    derived_binary=list(derived_temp_binary.__reversed__())
    return int(list_of_nb_to_str(derived_binary),2)

print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))

    
