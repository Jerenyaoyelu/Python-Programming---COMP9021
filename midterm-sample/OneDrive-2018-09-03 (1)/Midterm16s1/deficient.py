import sys


def check_deficient(n):
    divisors = []
    for i in range(1,n):
        if n%i ==0:
            divisors.append(i)

    if n > sum(divisors):
        return True
    else:
        return False

try:
    a, b = [int(i) for i in input('Enter two strictly positive numbers: ').split()]
    if a <=0 or b <= 0:
        raise ValueError

except ValueError:
    print('Incorrect input, giving up.')
    sys.exit

num_array = [n for n in range(1,max(a,b)+1)]

for n in range(min(a,b),max(a,b)++1):
    if check_deficient(n):
        num_array[num_array.index(n)] = 0

num_array.append(None)
consec = []
max_consec = []
consec_numbers = 0
for i in range(len(num_array)):
    if num_array[i] == 0:
        consec.append(i+1)
    
    if num_array[i] != 0 and consec:
        max_consec.append(consec)
        consec = []

for i in max_consec:
    if len(i) > consec_numbers:
        consec_numbers = len(i)
        max_array = i

if consec_numbers == 0:
    if b > a:
        print(('There is no deficient number between {} and {}.').format(a,b))
    else:
        print(('There is no deficient number between {} and {}.').format(b,a))
elif b> a:
    print(('The longest sequence of deficient numbers between {} and {} ranges between {} and {}.').format(a,b,max_array[0],max_array[-1]))
else:
    print(('The longest sequence of deficient numbers between {} and {} ranges between {} and {}.').format(b,a,max_array[-1],max_array[0]))
