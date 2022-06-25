import math
import itertools
def solution(numbers):
    answer = {}
    cnatUseNumber = {0:True ,1:True } 
    length = len(numbers)
    def isPrime(number):
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0 :
                return False
        return True 

    for i in range(1,length+1):
        for number in itertools.permutations(numbers, i):
            number =   int(''.join(number))
            if answer.get(number) : 
                continue 
            if cnatUseNumber.get(number):
                continue 
            if isPrime(number) :
                answer[number] = True
            else :
                cnatUseNumber[number] = True     
    return len(answer.keys())
  
  
 # itertools.permutations(numbers, i) 안에 중복을 제거하면 더 빠르다 라고 생각했음 
# 다른 풀이
import itertools
def solution(numbers):
    answer,cantAnswer = {} , {0:True , 1 : True}
    def isPrime(number):
        for i in range(2, int(pow(number,0.5)) + 1 ):
            if number % i == 0 :          
                cantAnswer[number] =True
                return
        answer[number] = True
    for i in range(len(numbers)):
        [ isPrime(n)  for n in set(map(int, map("".join, itertools.permutations(numbers, i + 1)))) if not answer.get(n) and not cantAnswer.get(n)  ]
    return len(answer.keys())
  
  # 나는 answer , cantAnswer로 이미 중복 체크 로직이 존재함, 따라서 중복을 2번 체크한다 => 비효율적
  
import itertools
def solution(numbers):
    answer,cantAnswer = {} , {0:True , 1 : True}
    def isPrime(number):
        for i in range(2, int(pow(number,0.5)) + 1 ):
            if number % i == 0 :          
                cantAnswer[number] =True
                return
        answer[number] = True
    for i in range(len(numbers)):
        [ isPrime(n)  for n in map(int, map("".join, itertools.permutations(numbers, i + 1))) if not answer.get(n) and not cantAnswer.get(n)  ]
    return len(answer.keys())
