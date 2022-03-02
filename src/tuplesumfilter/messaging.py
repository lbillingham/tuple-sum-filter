"""before we design a messaging system, 
we need to search for a given word
or set of words in all our messages
"""

from typing import List, Set

Id = int

'''
id  | message                                             | other fields...  
----------------------------------------------------------|-----------------
1   | Hi Fred, how are you?                               |
2   | How do I add a new method to the API                |
3   | You need to follow the process defined on the wiki  |
.     ...
.     ...
1B  | ...                                                 |

      a
you: [1, 3, 6, 10]
the: [2, 3, 5, 6, 11]
      b
'''



def search(word: str, messages: dict[Id,str]) -> List[Id]:
    """We'd really do a post-write job to populate a 2nd DB 
    table that 1:many mapped word->[message_id] so we 
    could do fast lookup
    """
    return [idx for idx, mess in messages if word in message]


def intersect_original(A: List[Id], B: List[Id]) -> List[Id]
    """O(n*m) where n and m are lengths of the lists of ids"""
    C = []
    for a in A:
        for b in B:
            if a == b:
                C.append(a)
    return C


def intersect_better(A: List[Id], B: List[Id]) -> Set[Id]:
    """O(n) + O(m) + O(m) where n and m are lengths of the lists of ids
    requires extra storage for sets"""
    return set(A).intersection(set(B))

    #creating a set O(n) + O(m) + fo))


def intersect_even_better(A: List[Id], B: List[Id]) -> List[Id]:
    """Assuming ids are already sorted, we can do O(m*n)
    without the extra storage of a set
    We track 2 list indicies and shuffle 
    when there we've exhasted the available less than nums
    """
    # assume that the lists are already sorted
    # by someone doing
    # sort(A)
    # sort(B)
    
    C = []
    
    while ia < len(A) and ib < len(B):
        if A[ia] == B[ib]:
            C.append(A[ia])
            ia += 1
            ib += 1
        elif A[ia] > B[ib]:
            ib += 1
        else:
            ia += 1
    return C
