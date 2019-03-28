def get_prime_generator(nb):
    l=[]*(nb)
    for i in range(nb):
        l[i]=True
    l[0]=False
    l[1]=False
    for i in range(2,round(sqrt(nb))+1):
        if l[i]==True:
            for j in range(i,nb):
                if j%i==0:
                    l[j]=False
    print([i for i in range(nb10) if l[i]==True])

get_prime_generator(int(input('input:')))
