# Lab1-1
# Written by Jeren Lu for COMP9021 Lab Exercise

min_t=0
max_t=100
step=10

print('Celsius\tFahrenheit')
for Celsius in range(min_t,max_t+10,10):
    Fahrenheit=Celsius*9/5+32
    print('%7d\t%10.0f'%(Celsius,Fahrenheit))
