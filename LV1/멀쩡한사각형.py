# https://programmers.co.kr/learn/courses/30/lessons/62048
# 많이 어려움 ㅋㅋ
import math
def solution(w,h):
    answer = 0

    # (0,0) -> (2,3) -> (4,6) -> (6,9) -> (8,12) gcd = 4 
    # (0,0) -> (1,2) -> (2,4) gcd = 2
    # w * h - (w+h - gcd) 
    return w*h - ( w+h - math.gcd(w,h))