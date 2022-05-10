def solution(numbers, hand):
    answer = []
    phone = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]
    left=[3,0]
    right = [3,2]
    def append(hand,index):
        answer.append(hand)
        return index

    for n in numbers:
        if n%3 == 1:
            answer.append("L")
            left =  [round(n/4) ,0]
        elif n!=0 and  n%3 == 0 : 
            answer.append("R")
            right  = [(n/3)-1,2]
        else  : 
            x = 3 if n== 0 else round(n/4)
            index = [x,1]
            l_d = abs(left[0]-index[0])+abs(left[1]-index[1])
            r_d = abs(right[0]-index[0])+abs(right[1]-index[1])
            if l_d == r_d :
                if hand == "right": 
                     right =append("R",index)
                else :
                    left =append("L",index)
            elif l_d > r_d :
                 right =append("R",index)
            else :
                 left = append("L",index)
                    
            
                
    return ''.join(answer)