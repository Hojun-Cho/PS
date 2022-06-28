## 처음 풀이 
def solution(enroll, referral, seller, amount):
    answer={}
    referrals = {}
    def calculate(now_money,now_people):
        if referrals[now_people] == "-" :
            if now_money * 0.1 < 1 :
                answer[now_people] += now_money 
            else :
                now_money -= int(now_money*0.1) 
                answer[now_people] += now_money 
            return 0
        if now_money * 0.1 < 1 :
            answer[now_people] += now_money 
            return 0
        next_money = int(now_money*0.1)
        answer[now_people] += (now_money - next_money)
        return next_money
    for i in range(len(enroll)) :
        answer[enroll[i]] = 0
        referrals[enroll[i]] = referral[i]

    for i in range(len(seller)) : 
        people,count = seller[i] , amount[i] 
        now_people ,now_money = people , count *100 
        while True :
            result = calculate(now_money,now_people)
            if result == 0 :
                break 
            now_people,now_money = referrals[now_people],result


    return list(answer.values())

## 다음 풀이 
def solution(enroll, referral, seller, amount):
    answer,peoples = {} ,{}
    def calculate(now_money,now_people):
      referral = now_money * 0.1
        if referral < 1 :
            answer[now_people] += now_money 
            return 0
        if peoples[now_people] == "-" :
            answer[now_people] += now_money -int(referral)
            return 0
        answer[now_people] += (now_money - int(referral))
        return int(referral)
    
    for i in range(len(enroll)) :
        answer[enroll[i]] = 0
        peoples[enroll[i]] = referral[i]
        
    for now_people,count in zip(seller,amount): 
        now_money = count *100 
        while True :
            result = calculate(now_money,now_people)
            if result == 0 :
                break 
            now_people,now_money = peoples[now_people],result
    return list(answer.values())
