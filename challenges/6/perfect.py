# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

# Insert your code here

try:
    nb=int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
def isperfect(n):
    sum=0
    for i in range(2,n+1):
        if n%i==0:
            sum += n/i
    if sum==n:
        return True
    else:
        return False

for i in range(1,nb+1):
    if isperfect(i):
        print(f'{i} is a perfect number.')