from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0;
    while (location <= n-1 && S[location] != x)
        location++;
    if (location > n-1)
    location = -1;
    

    return location
