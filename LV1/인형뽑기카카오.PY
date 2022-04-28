def solution(board, moves):
    answer = 0
    stack = []
    stack_len=0
    N = len(board[0])
    
    for i,n in enumerate(moves):
        n-=1
        j=0
        while j<N :
            if board[j][n] == 0 :
                j+=1 
            elif board[j][n] >0 :
                now_num= board[j][n] 
                if stack_len>0 and stack[-1] ==now_num :
                    stack.pop()
                    stack_len-=1
                    answer +=2 
                else :
                    stack.append(now_num)
                    stack_len +=1
                    
                board[j][n] = 0 
                break

                
    return answer 
                