def solution(brown, yellow):
    target = brown + yellow 
    for i in range(3,int(target**0.5) +1 ):
        x = i  # 세로            3         4   6 
        y = target / i # 가로    8        12    8  
        if  x >y :
            continue
        if (x-2) * (y-2) == yellow :
            if x * y  == target :
                return [y,x] 
        
