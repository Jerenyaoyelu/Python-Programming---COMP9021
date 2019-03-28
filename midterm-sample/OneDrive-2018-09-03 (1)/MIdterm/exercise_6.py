import sys


def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''
    if a <= 0 or b < a:
        sys.exit()

    for i in range(a,b+1):
        for j in range(i,b+1):
            if iseven(i+j):
                i_list = [int(k) for k in str(i)]
                i_init = -1
                i_test = True
                for d in i_list:
                    if i_init <0:
                        i_init = d
                    elif d<=i_init:
                        i_test = False
                if i_test:
                    j_list = [int(k) for k in str(j)]
                    j_init = -1
                    j_test = True
                    for d in j_list:
                        if j_init <0:
                            j_init = d
                        elif d<=j_init:
                            j_test = False

                    if j_test:
                        mean = (i+j)//2
                        mean_l = [int(k) for k in str(mean)]
                        increase = False
                        if len(mean_l)>1:
                            if mean_l[1] > mean_l[0]:
                                increase = True
                        if increase:
                            mean_test = True
                            m_init = -1
                            for d in mean_l:
                                if m_init <=0:
                                    m_init = d
                                elif d<m_init:
                                    mean_test = False
                        else:
                            mean_test = True
                            m_init = -1
                            for d in mean_l:
                                if m_init <0:
                                    m_init = d
                                elif d>= m_init:
                                    mean_test = False
                        if mean_test:
                            print(i,'and',j,'with',mean,'as average')

                            
            

def iseven(n):
    even = True
    if n%2 ==0:
        even = False
    return even
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
