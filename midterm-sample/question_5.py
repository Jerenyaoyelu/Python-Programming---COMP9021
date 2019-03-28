

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    string_dict={}
    # Insert your code here
    for i in range(len(word)):
        count_len=1
        if i ==len(word)-1:
            string_dict[word[i]]=count_len
        else:
            for j in range(i+1,len(word)):
                if ord(word[j])-ord(word[j-1])==1:
                    count_len +=1
                else:
                    string_dict[word[i:j]]=count_len
                    count_len=1
                    break
            if count_len>1:
                #if dont reset count_len in the  'else' condition, then the following command is needed.
                #Or, it will add every string started from i position to the dictionary.
                #string_dict[word[i:i+count_len]]=count_len
                #in fact, reset count_len is better, because it can avoid meaningless running(adding meaningless string to the dictionary).
                string_dict[word[i:]]=count_len
    desired_length=max(string_dict.values())
    for i in range(len(word)):
        if word[i:i+desired_length] in string_dict:
            desired_substring=word[i:i+desired_length]
            break
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
