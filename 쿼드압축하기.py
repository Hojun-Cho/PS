def solution(arr):
    result = [0,0]
    def invoke(x,y,size) :
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j] != arr[x][y] :
                    size= size//2
                    invoke(x,y,size)
                    invoke(x,y+size,size)
                    invoke(x+size,y,size)
                    invoke(x+size,y+size,size)
                    return 
        result[arr[x][y]] +=1 

    size = len(arr[0])
    invoke(0,0,size)
    return result
