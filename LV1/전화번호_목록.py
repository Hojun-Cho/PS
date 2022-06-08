### 사전순으로 정렬하면 동일한 접두사를 가진 문자열에서 더 짧은 문자열이 앞에 나온다. 만약 11 110 113 의 경우 
### 굳이 113 까지 가지 않아도 110 에서 return False를 하면 결과가 나온다. 따라서 사전순으로 정렬하면 문제가 풀린다
def solution(phone_book):
    dic =[]
    phone_book.sort()
    [dic.append(len(n)) for n in phone_book]
    for i in range( len(phone_book)-1) :
        if phone_book[i] in phone_book[i+1][:dic[i]]:
            return False
    return True
