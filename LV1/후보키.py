from  itertools import combinations
rel={}
def get(arr,key,ben):
    result = []
    for i in range(len(key)):
        for x in combinations(key,i+1):
            if rel.get(x) :
                return 0;
    result = [ arr[i] for i in key ]        
    return ''.join(result)
    
            

def solution(relation):
    # 처음엔 다 선택 점점 하나씩 줄여간다
    col = len(relation[0])
    row = len(relation)
    arr = [i for i in range(0,col)]
    ben = [False for _ in range(col)]
    answer = 0
  
    # 유일성이 없는 키를 기억
    for i in range(col):
        last = {}
        for j in range(row):
            if last.get(relation[j][i]) :
                ben[i] =True
                break;
            last[i] = 1


    for i in range(col):
        for x in combinations(arr,i+1):
            dic ={} 
            result = True 
            # 하나라도 깨지면 바로 out 
            for j in range(row):
                temp = get(relation[j],x,ben)
                if not temp or  dic.get(temp) :
                    result =False
                    break # 유일성이 없는 경우 
                dic[temp]=1
                    
            if result : 
                rel[x] = 1 
                answer +=1 

    return answer