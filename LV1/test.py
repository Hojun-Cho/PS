

def cal_point(now,_next):
    bottom = now[0]*_next[1] - now[1]*_next[0]
    x=( now[1]*_next[2] - now[2]*_next[1])
    y= (now[2]*_next[0] - now[0]*_next[2])
    if x%bottom == 0 and y%bottom== 0:
        return [x//bottom,y//bottom]
    return None
def solution(lines):
    board =[]    
    for i in range(len(lines)-1 ):
        line_now = lines[i]   
        for line_next in lines[i+1:] :
            point =  cal_point(line_now,line_next)
            if not point : 
                continue
            board.append(point)
    points=  set(list(map(tuple,board)))
    x_min =min(points,key=lambda x:x[0])[0]
    x_max = max(points,key =lambda x:x[0])[0]
    y_min = min(points,key = lambda y:y[1])[1]
    y_max = max(points,key = lambda y:y[1])[1]

    answer =[ [] for i in range(y_max-y_min)]
    print(answer)
    for i in range(y_max-y_min):
        for j in range(x_max-x_min):
            answer[i].append( '.')
    for x,y in points:

        answer[y+abs(y_min)][x+abs(x_min) ] = "*"
    return [''.join(ans) for ans in answer ]

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])