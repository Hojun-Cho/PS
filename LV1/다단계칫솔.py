# 자신보다 위에 있는 아이들을 배열에 넣는다
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
