def solution(d, budget):
    d.sort()
    x= [i+1 for i,x in enumerate(d)if sum(d[:i+1])<=budget]
    return x[-1] if x  else 0
