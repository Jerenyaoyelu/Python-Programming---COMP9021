# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# If i, j and k are numbers in the range [10, 99], i < j < k,
# and every digit occurs at most once in i, j and k
# then 10 <= i <= 76, j <= 87, and k <= 98. 
min_i = 10
max_i = 76
max_j = 87
max_k = 98

for i in range(min_i, max_i + 1):
    i_digits = {i // 10, i % 10}
    if len(i_digits) != 2:
        continue
    for j in range(i + 1, max_j + 1):
        i_and_j_digits = i_digits.union((j // 10, j % 10))
        if len(i_and_j_digits) != 4:
            continue           
    # Insert your code here to generate k,
    # check that it satisfies the desired conditions,
    # and check that i * j * k also satisfies the desired condition,
    # in which base one solution is ouput.
