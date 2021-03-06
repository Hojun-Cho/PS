# # https://programmers.co.kr/learn/courses/30/lessons/17677
# import sys
# def divide(string):
#     dic ={}
#     arr=[]
#     for i in range(len(string)-1):
#         a,b=string[i],string[i+1] 
#         if a.isalpha() and b.isalpha() :
#             result = a+ b
#             dic[result] =dic[result] +1 if dic.get(result) else 1 
#             arr.append(result)    
        
#     return arr,dic
# def solution(str1, str2):
#     arr1,dic1= divide(list(str1.lower()))
#     arr2,dic2= divide(list(str2.lower()))    
    
#     _set = set(arr1+arr2)
    
#     #중복 => min이 교집함    
#     x=y=0
#     print(_set,dic1,dic2)
#     for key in _set:
#         if dic1.get(key) and dic2.get(key) :
#             duplicate1 = dic1[key]
#             duplicate2 = dic2[key]
#             x += min(duplicate1,duplicate2)
#         duplicate1 = dic1[key] if dic1.get(key) else 0
#         duplicate2 = dic2[key] if dic2.get(key) else 0
#         y += max(duplicate1,duplicate2) 
#         print(x,y)
#     if y == 0:
#         return 1*65536 
#     return ((x/y) * 65536)//1

def divide(string):
    dic ={}
    for i in range(len(string)-1):
        a,b=string[i],string[i+1] 
        if a.isalpha() and b.isalpha() :
            result = a+ b
            dic[result] =dic[result] +1 if dic.get(result) else 1 
    return dic

def solution(str1, str2):
    dic1= divide(list(str1.lower()))
    dic2= divide(list(str2.lower()))    
    _set = set(list(dic1.keys())+list(dic2.keys()))
    
    #중복 => min이 교집함    
    x=y=0
    for key in _set:
        if dic1.get(key) and dic2.get(key) :
            duplicate1 = dic1[key]
            duplicate2 = dic2[key]
            x += min(duplicate1,duplicate2)
        duplicate1 = dic1[key] if dic1.get(key) else 0
        duplicate2 = dic2[key] if dic2.get(key) else 0
        y += max(duplicate1,duplicate2) 
    if y == 0:
        return 1*65536 
    return ((x/y) * 65536)//1

def divide(string):
    dic ={}
    for i in range(len(string)-1):
        result =''.join(string[i:i+2])
        if result.isalpha() :
            dic[result] =dic[result] +1 if dic.get(result) else 1 
    return dic

def solution(str1, str2):
    
    
    dic1= divide(list(str1.lower()))
    dic2= divide(list(str2.lower()))    
    _set = set(list(dic1.keys())+list(dic2.keys()))
    
    #중복 => min이 교집함    
    x=y=0
    for key in _set:
        duplicate1 = dic1.get(key)
        duplicate2 = dic2.get(key)
        if  duplicate1 and duplicate2  :
            x += min(duplicate1,duplicate2)
        duplicate1= 0 if not duplicate1 else duplicate1 
        duplicate2 =0 if not duplicate2 else duplicate2
        y += max(duplicate1,duplicate2) 
    if y == 0:
        return 1*65536 
    return ((x/y) * 65536)//1    