def solution(n, words):
    answer = []
    dic = {}
    last = words[0][0] 
    for i,word in enumerate(words) :
        if  last[-1] != word[0]  or  dic.get(word) : 
            return [i%n +1 ,  i//n +1]
        dic[word]=1
        last= word 
    return [0,0]
