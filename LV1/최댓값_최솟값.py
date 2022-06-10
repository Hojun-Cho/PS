def solution(s):
    x= sorted(list(map(int,s.split(" "))))
    return ' '.join(map(str,[x[0],x[-1]]))
