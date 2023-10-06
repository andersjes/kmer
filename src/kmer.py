"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    kmers = []
    for i in range(0,len(x)-k+1):
        kmers.append(x[i:i+k])
          
    return kmers




    """
        Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """



print (kmer('agtagtcg', 3))



def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    """
    ...


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    ...