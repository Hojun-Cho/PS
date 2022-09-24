from itertools import product

def solution(word):
    words =[] 
    for count in range(1,5+1):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=count):
            words.append("".join(c))
    words.sort()
    return words.index(word)+1
