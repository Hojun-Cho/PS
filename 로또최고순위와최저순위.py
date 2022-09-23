def solution(lottos, win_nums):
    answer = []
    wins = {key:True  for key in win_nums}
    count = 0 
    for l in lottos :
        if l!=0 and wins.get(l):
            del wins[l]
        if l == 0 :
            count +=1 
    best = len(wins) - count 
    worst = len(wins)
    return [valid(best),valid(worst)]

def valid(num) -> int:
    return num+1 if num+1 <= 6 else num 
