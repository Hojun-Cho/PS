### A의 순서에 B를 맞춘다 
### 즉 A가 어떻게 주어지던 상관 없다. 단지 A를 이길 수 있는 B만 SORT 후 매칭하면 정답이 나온다 
def solution(A, B):
    answer=0
    A.sort()
    B.sort()
    while A   and B  :
        if A[-1] < B[-1] :
            answer +=1 
            B.pop()
            A.pop()
        elif A[-1] >= B[-1] :
            A.pop()
    return answer
