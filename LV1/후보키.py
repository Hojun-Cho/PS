from  itertools import combinations
# 보다적은후보키가나오면사용 xx
rel={}
def get(arr,key,ben):
    result = []
    _len = len(key)
    for i in range(_len):
        for x in combinations(key,i+1):
            if rel.get(x) :
                return 0;
    for i in key:
        result.append(arr[i])
        
    return ''.join(result)
    
            

def solution(relation):
    # 처음엔 다 선택 점점 하나씩 줄여간다
    col = len(relation[0])
    row = len(relation)
    arr = [i for i in range(0,col)]
    ben = [False for _ in range(col)]
    answer = 0
    relation.sort()
  
    for i in range(col):
        last = -1 
        for j in range(row):
            if last == relation[j][i] :
                ben[i] =True
                break;
            last =relation[j][i]


    for i in range(col):
        for x in combinations(arr,i+1):
            dic ={} 
            result = True 
            # 하나라도 깨지면 바로 out 
            for j in range(row):
                temp = get(relation[j],x,ben)
                if not temp or  dic.get(temp) :
                    result =False
                    break
                dic[temp]=1
                    
            if result : 
                rel[x] = 1 
                answer = max(answer,i+1)
            else : 
                rel[x]=0
    return answer 



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]));