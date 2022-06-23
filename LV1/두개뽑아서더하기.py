def solution(numbers):
    length = len(numbers)
    answer = []
    for i in range(length-1):
        [answer.append(numbers[i]+numbers[j]) for j in range(i+1,length)]
    return sorted(list(set(answer)))
