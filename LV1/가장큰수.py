# reverse 정렬을 통해서 푼다.
# '104' '1' => '1041' < '1104' 이를 위해서는 a+b 또는 b+a중 어떤것이 더 큰지 알아야 한다
# 따라서 현재 위치에서 뒤로 가면서 swap이 가능한지 살핀다.
# 하지만 이렇게 풀면 시간 초과가 발생한다 O (n^2)
# 따라서 공간 복잡도를 크게 잡더라도 x*3 을 해서 사이즈를 맞춰서 비교한다
# 만약 1과 104를 비교한다면 '111' '104104104'를 비교한다.
# 각각의 인덱스로 비교한다
# 0 : 동일
# 1 : '111'이 더 크다
# 결과로 1을 더 앞에 배치한다. 더 큰 문자가 앞에 와야지 최대값이 된다.
def solution(numbers):
#     def is_okay_swap(a,b):
#         return str(a)+str(b) > str(b)+str(a)
#     index = 1 
#     numbers.sort(reverse=True)
#     _len = len(numbers)
#     while index < _len:
#         i = index
#         while i>0  and is_okay_swap(numbers[i],numbers[i-1]) : 
#             numbers[i-1],numbers[i] = numbers[i],numbers[i-1]
#             i-=1 
            
#         index+=1
    numbers =list(map(str,numbers))
    numbers.sort(key=lambda x:x*3 ,reverse=True)
    return  str(int(''.join(numbers)))
