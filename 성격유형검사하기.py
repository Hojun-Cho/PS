from collections import defaultdict

indis =[]

def solution(survey, choices):
    global indis 
    answer = []
    indi_1 = {"R":0,"T":0}
    indi_2 = {"C":0,"F":0}
    indi_3 = {"J":0,"M":0}
    indi_4 = {"A":0,"N":0}
    indis = [indi_1,indi_2,indi_3,indi_4]

    for sur,choice in zip(survey,choices):
        Add(sur,choice)
    return "".join([sorted(indi.items(),key=lambda x:x[1],reverse = True)[0][0] \
        for indi in indis  ])
 
def Add(survey,choice) :
    x,y= list(survey)
    global indis 
    if choice <=3 :
        Get(x)[x] += (4-choice) 
    else :
        Get(y)[y] += (choice-4) 
    
def Get(x):
    global indis 
    for indi in indis :
        for key in indi.keys() :
             if key == x:
                return indi 
    
