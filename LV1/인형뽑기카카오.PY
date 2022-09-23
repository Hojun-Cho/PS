Board = [] 
Height = 0 
def solution(board, moves):
    global Board,Height
    Board,Height = board ,len(board)
    stack = []
    answer = 0
    for row in moves:
        result = pull_up(row-1)
        if result != 0 :
            answer+=push(stack,result)
    return answer 
            
def pull_up(row):
    global Board,Height
    for h in range(Height):
        if Board[h][row] != 0 :
            x,Board[h][row] = Board[h][row],0
            return  x 
    return 0 

def push(answers,target):
    index,count= len(answers) -1 ,0
    while index >= 0 and answers[index] == target :
        count +=1 
        index -=1 
    if count == 0 :
        answers.append(target)
        return 0
    answer = 1 
    for i in range(count):
        answers.pop()
        answer +=1 
    return answer 
