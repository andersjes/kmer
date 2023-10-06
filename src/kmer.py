"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.
    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    kmers = []
    for i in range(0,len(x)-k+1):
        kmers.append(x[i:i+k])
          
    return kmers







def unique_kmers(x: str, k: int) -> list[str]:

    """
    Computer all unique k-mers of x.
    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """

    kmers = []
    unique = []
    for i in range(0,len(x)-k+1):
        kmer = x[i:i+k]
        kmers.append(kmer)
    for j in kmers:
        if j not in unique:
            unique.append(j)

    return unique


    ...


def count_kmers(x: str, k: int) -> dict[str, int]:
    

    """
    Computer all k-mers of x and count how often they appear.
    >>> count _kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}




    FIXME: do you want more tests here?
    """
    kmers = []
    count = {}
    for i in range(0,len(x)-k+1):
        kmer = x[i:i+k]
        kmers.append(kmer)
    for j in kmers:
        if j not in count:
            count[j] = 1
        else:
            count[j] += 1
    return count
    
    
    ...

print (count_kmers ('agtagtcg', 3))