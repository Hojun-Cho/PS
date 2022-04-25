# def list_to_dic(arr):
#     l = dict()
#     for i in range(6) :
#         if not l.get(arr[i]) :
#              l[arr[i]] = 1 

#         elif arr[i] == 0  :
#             l[arr[i]] +=1 

#     return l 

# def None_to_Zero(num):
#     if not num : 
#         return 0 
#     return num 
# def make_answer(num):
#     if num >=7 :
#         return 6
#     return num 
    
# def solution(lottos , win_nums):
#     max_rank=7
#     min_rank =7
#     answer= []
    
#     dic_lottos= list_to_dic(lottos)
#     dic_win  = list_to_dic(win_nums) 
    
#     for key in dic_lottos.keys():
#         same = dic_win.get(key)
#         if same :
#             max_rank-=1 
#             min_rank -= 1 

#     my_zero_count = None_to_Zero(dic_lottos.get(0)) 
#     win_zero_count =None_to_Zero( dic_win.get(0))
    

#     if win_zero_count -my_zero_count > 0 :
#         max_rank -= my_zero_count
        
#     elif win_zero_count - my_zero_count < 0 :
#         max_rank -=my_zero_count

#     else :
#         max_rank -= win_zero_count 

#     answer.append(make_answer(max_rank))
#     answer.append(make_answer(min_rank))
#     return answer 
    



    
def solution(lottos,win_nums):
    max_rank = 6 
    min_rank = 6     
    rank = [1,2,3,4,5,6,6]
    zero_count = lottos.count(0)

    for item in win_nums :
        if item in lottos :
            max_rank -=1 
            min_rank -=1 
            
    max_rank =rank[max_rank-zero_count]
    min_rank =rank[min_rank]
    
    print(max_rank,min_rank)
    return [max_rank,min_rank]
    


solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]	)