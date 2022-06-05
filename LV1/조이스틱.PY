# 1. 계속 오른쪽으로 가는 경우   A B B A
# 2. 오른쪽으로 가다가 왼쪽으로 돌아 가는 경우 B A A A B 
# 3. 왼쯕으로 가다가 오른쯕으로 돌아 가는 경우 B B B A A B   => 
# 3-1 . 인덱스 2번에서  오른쪽으로 가다가 왼쪽으로 가는 경우 => 2 * 2 + 1 = 5 
# 3-2 . 인덱스 2번에서 왼쪽으로 가다가 오른쪽으로 가는 경우  => 2 + 1*2 =4
# 주의 # 만약  B B A C D의  인덱스 2에서 <- <- 후 D에서 -> 해서인덱스 0로 돌아오는 일은 어떠한 경우에도 최선이 될 수 없다.
# 만약 그런 일이 발생하면 왔던 길을 3번 밟게된다 
def solution(name):
    answer = 0
    input_length = len(name)
    min_dist = input_length -1 
    for i,n in  enumerate(name) : 
        answer += min(ord(n) - ord('A'),ord('Z') - ord(n) +1)
        next_i =i+1 
        while next_i <input_length and name[next_i] == 'A':
            next_i +=1 
        min_dist = min(min_dist,i*2 + input_length - next_i,i+ 2*(input_length-next_i))
    
    return answer +min_dist
