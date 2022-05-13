def initArray(rows,columns):
    size = max(rows,columns)
    arr =[[0]*(size+1) for _ in range(size+1)] 
    num = 0
    for i in  range(1,rows+1) :
        for j in range(1,columns+1) :
            num+=1 
            arr[i][j] = num
    return arr
def solution(rows, columns, queries):
    answer = []
    arr =  initArray(rows,columns)

    for x_s,y_s ,x_e,y_e  in queries :
        last=temp = arr[x_s][y_s] 
        for y in range(y_s+1,y_e+1) :
            if y <=  rows :
                arr[x_s][y],last= last,arr[x_s][y]
                temp = min(temp,last)
        for x in range(x_s+1,x_e+1) :
            if x <= columns :
                arr[x][y_e] ,last = last , arr[x][y_e] 
                temp = min(temp,last)
        for y in range(y_e-1,y_s-1,-1):
            if y > 0 :
                arr[x_e][y] ,last = last,arr[x_e][y] 
                temp = min(temp,last)
        for x in range(x_e-1,x_s-1,-1):
            if x > 0 : 
                arr[x][y_s],last = last,arr[x][y_s] 
                temp = min(temp,last) 
            
        answer.append(temp)       
    return answer 
                    

                    
# solution(6,6        ,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
# solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100,	97	,[[1,1,100,97]])