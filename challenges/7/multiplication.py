# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.
def nb_to_list(n):
    l=[0]*4
    t=divmod(n,10)
    for i in range(len(l)-1,-1,-1):
        l[i]=t[1]
        t=divmod(t[0],10)
    return l
for i in range(100,1000):
    for j in range(10,100):
        matrix=[[0]*4]*5
        if i*(j//10*10)<10000 and i*j%10+i*(j//10*10)<10000:
            matrix[0]=nb_to_list(i)
            matrix[1]=nb_to_list(j)
            matrix[2]=nb_to_list(i*(j%10))
            matrix[3]=nb_to_list(i*(j//10*10))
            matrix[4]=nb_to_list(i*(j%10)+i*(j//10*10))
            new_m=list(zip(*matrix))
            s=sum(new_m[0])
            val=True
            for k in range(len(matrix[0])):
                if s!=sum(new_m[k]):
                    val=False
            if val==True:
                print(f'{i}*{j}={i*j},all columns adding up to {s}.')