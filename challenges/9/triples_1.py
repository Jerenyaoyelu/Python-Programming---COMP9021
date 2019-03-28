# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here
def split_numb(n):
    l=set()
    while n !=0:
        l.add(n%10)
        n=n//10
    return l
for i in range (10,77):
    for j in range(i+1,88):
        for k in range(j+1,99):
            digits=split_numb(i)|split_numb(j)|split_numb(k)
            product=split_numb(i*j*k)
            if len(digits)==6 and digits==product:
                print(i,j,k)
