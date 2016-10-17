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

def base_frequency(strand):
    """return frequency of dna base occurrence

    DNA is made up of four bases: guanine (G), adenine (A), thymine (T), or cytosine (C)
    this function analyzes a DNA strand and returns a report of the number of times each base occurs

    >>> base_frequency("AAAACCCGGT")
    'guanine (G):2, adenine (A):4, thymine (T):1, cytosine (C):3'

    >>> base_frequency("ACGT")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'

    >>> base_frequency("acgt")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'
    """
    dna = hist(strand.upper())
    results = 'guanine (G):{}, adenine (A):{}, thymine (T):{}, cytosine (C):{}'.format(dna['G'], dna['A'], dna['T'], dna['C'])
    return results


def reverse_strand(strand):
    """returns the reverse compliment of a strand

    >>> reverse_strand("AAAACCCGGT")
    'ACCGGGTTTT'

    >>> reverse_strand("aaaacccggt")
    'ACCGGGTTTT'

    """
    rev = list(strand.upper())
    dic = {"A": "T", "G": "C", "T": "A", "C": "G"}
    rev = [dic[n] if n in dic.keys() else n for n in rev]
    rev.reverse()
    rev = "".join(rev)
    return rev
    print rev
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
