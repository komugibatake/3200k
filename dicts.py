

def hist(s):
    """returns the histogram of the characters in s

    >>> hist("AAGGT")
    {'A': 2, 'T': 1, 'G': 2}

    >>> hist("!!xx")
    {'!': 2, 'x': 2}

    """
    x = {}
    for char in s:
        if char not in x:
            x[char] = 1
        else:
            x[char] += 1

    return x
    


def str_to_int(s):
    """converts a string to an integer value

    >>> str_to_int('s')
    115

    >>> str_to_int('st!ll')
    11511633108108L

    hint: the built in ord and chr functions

    """
    a = ""
    for item in s:
        a += str(ord(item))
    return int(a)


def null_list(length):
    """return a list of all None values of given length

    >>> null_list(3)
    [None, None, None]

    >>> null_list(1)
    [None]

    """
    n = []
    for item in range(length):
        n.append(None)
    return n

    #return [None] * length

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
