
first_num = []
for i in range(100,1000):
    digits_1 = [int(n) for n in str(i)]
    if digits_1[1]%2==0 and digits_1[2]%2 ==0:
        first_num.append(i)

second_num = []
for j in range(10,100):
    digits_2 = [int(n) for n in str(j)]
    if digits_2[0]%2 == 0 and digits_2[1]%2 == 0:
        second_num.append(j)
    
for i in first_num:
    for j in second_num:
        product = i*j
        if product >=1000 and product <10000:
            num1_list = [int(n) for n in str(i)]
            num2_list = [int(n) for n in str(j)]
            p1 = i*num2_list[1]
            if p1 >= 1000 and p1 < 10000:
                p1_digits = [int(n) for n in str(p1)]
                
                if p1_digits[0]%2 == 0 and p1_digits[1]%2 and p1_digits[2]%2 == 0 and p1_digits[3]%2 == 0:
                    p2 = i*num2_list[0]

                    if p2 >= 100 and p2 < 1000:
                        p2_digits = [int(n) for n in str(p2)]
                        
                        if p2_digits[0]%2 == 0 and p2_digits[1]%2 and p2_digits[2]%2 == 0:
                            p_digits = [int(n) for n in str(product)]
                            if p_digits[0]%2 and p_digits[1]%2 and p_digits[2]%2 == 0 and p_digits[3]%2 == 0:
                                print((' {}').format(i))
                                print(('x {}').format(j))
                                print(' ----')
                                print(p1)
                                print(p2)
                                print('-----')
                                print(product)
