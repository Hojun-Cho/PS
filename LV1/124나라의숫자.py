# https://programmers.co.kr/learn/courses/30/lessons/12899#
def solution(n):
   # divmod 를 이용한 문제, 단 0을 허용x따라서 0이 나오면  mod =4 로 설정하고
   # 몫에 -1을 해준다
   #  (5,0) =divmod(15,3) => mod =4 , n = 5-1
   #  (1,1) = divmod(4,3) => mod = 1 n =1 
   #  (0,1) = divmod(1,3) => mod = 1 n = 0 
   # => answer = "114" 
    answer = ''
    while n >0  :
        n,mod = divmod(n,3) #몫과 나머지
        if mod == 0 :
            n -=1 
            mod = 4
        answer += str(mod)
        

    return answer[::-1]