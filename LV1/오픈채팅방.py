# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다.
# 기존 로그도 변경된다
# record => 닉네임을 변경한 기록이 담긴 문자열 배열
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 최종적인 메세지를 출력해라 
from collections import defaultdict
dic= {}
answer = []
    
def make_log(command,answer) :
        
        if command[0] == "Enter" :
             answer.append([command[1] , "님이 들어왔습니다."])
        if command[0] =="Leave" :
             return answer.append([command[1] ,"님이 나갔습니다."])

        dic[command[1]]=command[2]
        
   
def solution(record):

        for i,n in enumerate(record):
            command= n.split()
            make_log(command,answer)
    
        for i,n in enumerate(answer):
            answer[i] = dic[n[0]] +n[1] 


        return answer