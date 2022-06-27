# 1차 풀이 
# 딕셔너리로 중복을 제거했다. 중복을 제거하는 더 근원적인 방법이 존재하는걸 왜 까먹었을까 !! 바로 set!! 
import collections
def solution(dirs):
    MAX ,MIN = 5,-5
    now_x,now_y = 0,0
    visit = collections.defaultdict(list)
    dic = {'L' :[0,-1] , 'R' : [0,1] ,'U' : [1,0] , 'D' : [-1,0] }
    answer = 0
    def isContain(x,y):
         return str(now_x+x) +str(now_y+y) not in visit[str(now_x)+str(now_y)] and str(now_x) +str(now_y) not in visit[str(now_x+x)+str(now_y+y)]
    for d in dirs : 
        x,y =  dic[d] 
        if -5<= now_x + x <=5 and  -5<= now_y + y <=5 :
            if isContain(x,y):
                visit[str(now_x)+str(now_y)].append(str(now_x+x) +str(now_y+y) ) 
                visit[str(now_x+x)+str(now_y+y)].append(str(now_x) +str(now_y) )
                answer +=1 
            now_x,now_y = now_x+x,now_y+y      
    return answer
  
  # 2차 풀이
  # set을 이용했다
import collections
def solution(dirs):
    now_x,now_y = 0,0
    visit = set()
    dir = {'L' :[0,-1] , 'R' : [0,1] ,'U' : [1,0] , 'D' : [-1,0] }
    for d in dirs : 
        next_x,next_y =  now_x+dir[d][0] , now_y + dir[d][1] 
        if -5<= next_x <=5 and  -5<= next_y<=5 :
            visit.add((now_x,now_y,next_x,next_y))
            visit.add((next_x,next_y,now_x,now_y))
            now_x,now_y = next_x,next_y
    return len(visit)//2
  
  #
  
  
