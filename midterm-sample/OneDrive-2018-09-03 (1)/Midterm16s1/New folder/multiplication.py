'''
Write a program that solves a multiplication
  O E E
x   E E
-----
E O E E
E O E
-------
O O E E
where E stands for an even digit and O stands for an odd digit. Of course the leading digit of any
of the 5 numbers cannot be 0. Two occurrences of E can refer to the same even digit or to two
distinct even digits, and two occurrences of O can refer to the same odd digit or to two distinct odd
digits.
The output of your program should be of the form above, with of course the Es and the Os being
replaced by appropriate digits. Still spaces are irrelevant; in particular, it is irrelevant whether
digits are separated by spaces, whether x (the multiplication sign) is followed by spaces, whether
there are leading spaces at the beginning of the last line. The number of - on the separating lines
is also irrelevant.
Your program should not make any assumption on the actual solution (which is unique), except
obvious ones on the ranges of some values.
'''

for i in range(100,1000,2):
    if not (i//10)%2 and (i//100)%2:
        for j in range(10,100,2):
            if not (j//10)%2:
                product = i*j
                if product <= 9988 and product >= 1100:
                    if not product%2 and not (product//10)%2 and (product//100)%2 and (product//1000)%2:
                        product_1 = i*(j%10)
                        if product_1 > 1000 and not product_1%2 and not (product_1//10)%2 and (product_1//100)%2 and not (product_1//1000)%2:
                            product_2 = i*(j//10)
                            if product_2 > 100 and not product_2%2 and (product_2//10)%2 and not (product_2//100)%2:
                                print(('  {}').format(i))
                                print(('x  {}').format(j))
                                print(' -----')
                                print((' {}').format(product_1))
                                print((' {}').format(product_2))
                                print(' -----')
                                print((' {}').format(product))
